import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Ride Analytics Dashboard")

df = pd.read_csv(
    r"D:\Guvi\Projects\ride_flow_ai\data\preprocessed\cleaned_rides.csv"
)

st.write(df.head())

fig = px.histogram(

    df,

    x='trip_distance',

    nbins=30,

    title="Trip Distance Distribution"
)

st.plotly_chart(fig)

fig2 = px.scatter(

    df,

    x='trip_distance',

    y='fare_amount',

    title="Fare vs Distance"
)

st.plotly_chart(fig2)