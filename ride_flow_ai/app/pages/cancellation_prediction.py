import streamlit as st
import joblib
import numpy as np

st.title("❌ Cancellation Prediction")

model = joblib.load(
    r"D:\Guvi\Projects\ride_flow_ai\models\cancellation_prediction_model.pkl"
)

eta = st.slider(
    "ETA",
    1,
    30,
    10
)

traffic = st.slider(
    "Traffic Level",
    1,
    10,
    5
)

rating = st.slider(
    "Driver Rating",
    1.0,
    5.0,
    4.5
)

surge = st.slider(
    "Surge Multiplier",
    1.0,
    3.0,
    1.5
)

distance = st.slider(
    "Trip Distance",
    1.0,
    30.0,
    5.0
)

fare = st.slider(
    "Fare Amount",
    50.0,
    1000.0,
    200.0
)

features = np.array([[
    eta,
    traffic,
    rating,
    surge,
    distance,
    fare
]])

prediction = model.predict(features)[0]

if prediction == 1:

    st.error("High Cancellation Probability")

else:

    st.success("Low Cancellation Probability")