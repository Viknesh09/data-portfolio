import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r"D:\Guvi\Projects\2nd project\literacy_project\data/adult_literacy.csv")

# Rename columns
df.columns = ["country", "code", "year", "adult_literacy"]

st.title("📊 Global Literacy Dashboard")

country = st.selectbox("Select Country", df["country"].unique())

filtered = df[df["country"] == country]

fig = px.line(filtered, x="year", y="adult_literacy")

st.plotly_chart(fig)