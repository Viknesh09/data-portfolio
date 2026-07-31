import streamlit as st

st.title("💰 Dynamic Pricing Engine")

base_fare = st.number_input(
    "Base Fare",
    value=100.0
)

demand = st.slider(
    "Demand Level",
    1,
    10,
    5
)

traffic = st.slider(
    "Traffic Level",
    1,
    10,
    5
)

surge = 1 + (demand * 0.1) + (traffic * 0.05)

final_price = base_fare * surge

st.metric(
    "Final Dynamic Price",
    f"₹ {final_price:.2f}"
)