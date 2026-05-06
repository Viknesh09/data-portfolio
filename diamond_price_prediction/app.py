import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd
import plotly.express as px

# ----------------------------
# PATH SETUP
# ----------------------------
BASE_DIR = os.path.dirname(__file__)
model_dir = os.path.join(BASE_DIR, "models")

# Optional dataset
data_path = os.path.join(BASE_DIR, "data", "sample_diamonds.csv")

# ----------------------------
# LOAD MODELS
# ----------------------------
model = joblib.load(os.path.join(model_dir, "regression_model.pkl"))
scaler = joblib.load(os.path.join(model_dir, "scaler.pkl"))

le_cut = joblib.load(os.path.join(model_dir, "le_cut.pkl"))
le_color = joblib.load(os.path.join(model_dir, "le_color.pkl"))
le_clarity = joblib.load(os.path.join(model_dir, "le_clarity.pkl"))

# ----------------------------
# LOAD DATA (OPTIONAL)
# ----------------------------
df = None
if os.path.exists(data_path):
    df = pd.read_csv(data_path)

# ----------------------------
# UI CONFIG
# ----------------------------
st.set_page_config(page_title="💎 Diamond Price Prediction", layout="wide")

st.title("💎 Diamond Price Prediction System")
st.caption("Predict diamond prices using Machine Learning")

st.markdown("---")

# ----------------------------
# TABS
# ----------------------------
tabs = ["🔮 Prediction"]

if df is not None:
    tabs.append("📊 Insights")

tab_objects = st.tabs(tabs)

# ============================
# 🔮 TAB 1: PREDICTION
# ============================
with tab_objects[0]:

    col1, col2 = st.columns(2)

    with col1:
        carat = st.slider("Carat", 0.1, 5.0, 1.0)
        x = st.number_input("Length (x)", 0.1, 10.0, 5.0)
        y = st.number_input("Width (y)", 0.1, 10.0, 5.0)
        z = st.number_input("Depth (z)", 0.1, 10.0, 3.0)

    with col2:
        cut = st.selectbox("Cut", le_cut.classes_)
        color = st.selectbox("Color", le_color.classes_)
        clarity = st.selectbox("Clarity", le_clarity.classes_)

    # Encoding
    cut_enc = le_cut.transform([cut])[0]
    color_enc = le_color.transform([color])[0]
    clarity_enc = le_clarity.transform([clarity])[0]

    # Feature Engineering
    volume = x * y * z

    features = np.array([[carat, cut_enc, color_enc, clarity_enc, 0, 0, x, y, z, volume, 0]])
    scaled = scaler.transform(features)

    if st.button("🔮 Predict Price"):
        try:
            price = model.predict(scaled)[0]

            # ✅ Improved Output
            st.success(f"💰 Estimated Price: ₹ {price:,.2f}")

            # ✅ Input Summary
            st.subheader("📋 Input Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"**Carat:** {carat}")
                st.markdown(f"**Cut:** {cut}")
                st.markdown(f"**Color:** {color}")

            with col2:
                st.markdown(f"**Clarity:** {clarity}")
                st.markdown(f"**Dimensions:** {x} × {y} × {z}")

            # ✅ Smart Insight
            st.subheader("💡 Insight")
            if price > 50000:
                st.info("💎 This is a high-value diamond")
            elif price > 20000:
                st.info("💎 This is a mid-range diamond")
            else:
                st.info("💎 This is a budget-friendly diamond")

        except Exception as e:
            st.error(f"Prediction Error: {e}")

# ============================
# 📊 TAB 2: INSIGHTS (OPTIONAL)
# ============================
if df is not None:
    with tab_objects[1]:

        st.subheader("📈 Price vs Carat")
        fig1 = px.scatter(df, x="carat", y="price", color="cut", opacity=0.5)
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("📊 Average Price by Cut")
        avg_price = df.groupby("cut")["price"].mean().reset_index()
        fig2 = px.bar(avg_price, x="cut", y="price", color="cut")
        st.plotly_chart(fig2, use_container_width=True)