import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.title("🌲 EcoType: Forest Cover Prediction")

st.write("Enter the details below:")

# Inputs
elevation = st.number_input("Elevation")
aspect = st.number_input("Aspect")
slope = st.number_input("Slope")
hydrology_h = st.number_input("Horizontal Distance to Hydrology")
hydrology_v = st.number_input("Vertical Distance to Hydrology")
road = st.number_input("Distance to Roadways")
hill_9 = st.number_input("Hillshade 9am")
hill_noon = st.number_input("Hillshade Noon")
hill_3 = st.number_input("Hillshade 3pm")
fire = st.number_input("Distance to Fire Points")
wilderness = st.number_input("Wilderness Area (encoded)")
soil = st.number_input("Soil Type (encoded)")

# Prediction
if st.button("Predict"):
    data = np.array([[elevation, aspect, slope, hydrology_h, hydrology_v,
                      road, hill_9, hill_noon, hill_3, fire,
                      wilderness, soil]])

    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)

    st.success(f"🌿 Predicted Forest Cover Type: {prediction[0]}")