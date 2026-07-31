import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(

    page_title="RideFlow AI",

    page_icon="🚖",

    layout="wide"
)

# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------

st.title("🚖 RideFlow AI Dashboard")

st.subheader(
    "Intelligent Ride Analytics, Forecasting & NLP Platform"
)

# ---------------------------------------------------
# HERO IMAGE
# ---------------------------------------------------

st.image(

    "https://images.unsplash.com/photo-1519501025264-65ba15a82390",

    use_container_width=True
)

# ---------------------------------------------------
# PROJECT DESCRIPTION
# ---------------------------------------------------

st.markdown("""

## 📌 Project Overview

RideFlow AI is an AI-powered intelligent ride analytics platform built using:

- Machine Learning
- NLP
- DistilBERT Transformers
- Recommendation Systems
- AI Chatbot Support
- Streamlit Deployment

The platform helps ride-sharing companies optimize:
- demand forecasting
- pricing strategies
- ride matching
- customer support
- sentiment analytics

""")

# ---------------------------------------------------
# FEATURE MODULES
# ---------------------------------------------------

st.markdown("## 🚀 Available AI Modules")

col1, col2 = st.columns(2)

with col1:

    st.info("📈 Demand Prediction")

    st.info("💰 Dynamic Pricing")

    st.info("❌ Cancellation Prediction")

    st.info("📊 Ride Analytics Dashboard")

with col2:

    st.info("🧠 DistilBERT Sentiment Analysis")

    st.info("🛠️ Issue Classification System")

    st.info("🚖 AI Ride Matching Assistant")

    st.info("🤖 AI Chatbot & Multilingual Support")

# ---------------------------------------------------
# PROJECT METRICS
# ---------------------------------------------------

st.markdown("## 📊 Model Performance")

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    "Demand Prediction R²",
    "0.90"
)

metric2.metric(
    "Cancellation Accuracy",
    "98%"
)

metric3.metric(
    "DistilBERT Accuracy",
    "90.6%"
)

# ---------------------------------------------------
# TECH STACK
# ---------------------------------------------------

st.markdown("## 🛠️ Technology Stack")

st.write("""

### Languages & Frameworks
- Python
- Streamlit

### Machine Learning
- Scikit-learn
- RandomForest
- Logistic Regression

### NLP & Deep Learning
- TF-IDF
- DistilBERT
- HuggingFace Transformers

### Visualization
- Plotly
- Matplotlib

### Dataset
- NYC TLC Taxi Dataset

""")

# ---------------------------------------------------
# BUSINESS USE CASES
# ---------------------------------------------------

st.markdown("## 💼 Business Use Cases")

st.success(
    "✔️ Intelligent Demand Forecasting"
)

st.success(
    "✔️ Dynamic Surge Pricing"
)

st.success(
    "✔️ Ride Cancellation Risk Analysis"
)

st.success(
    "✔️ Customer Sentiment Monitoring"
)

st.success(
    "✔️ Smart Driver Recommendation"
)

st.success(
    "✔️ AI Customer Support"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🚖 RideFlow AI")

st.sidebar.success(
    "Select any module from the sidebar pages."
)

st.sidebar.markdown("""

### Available Modules

- Demand Prediction
- Dynamic Pricing
- Cancellation Prediction
- Sentiment Analysis
- Analytics Dashboard
- Issue Classification
- Ride Matching Assistant
- AI Chatbot

""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "RideFlow AI | Intelligent Ride Analytics Platform"
)