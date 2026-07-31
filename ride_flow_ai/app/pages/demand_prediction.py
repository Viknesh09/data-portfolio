import streamlit as st
import joblib
import numpy as np

st.title("📈 Demand Prediction")

model = joblib.load(
    r"D:\Guvi\Projects\ride_flow_ai\models\demand_prediction_model.pkl"
)

hour = st.slider(
    "Hour of Day",
    0,
    23,
    12
)

trip_distance = st.slider(
    "Trip Distance",
    1.0,
    30.0,
    5.0
)

features = np.array([[
    hour,
    trip_distance
]])

prediction = model.predict(features)[0]

st.success(
    f"Predicted Demand: {prediction:.2f}"
)