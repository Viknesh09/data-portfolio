import streamlit as st
import sqlite3
import pandas as pd
from sql_queries import queries

conn = sqlite3.connect("db/database.db")

st.title("📊 Cross Market Dashboard")

menu = st.sidebar.selectbox("Menu", ["Overview", "SQL Runner"])

if menu == "Overview":
    df = pd.read_sql("SELECT * FROM crypto_prices LIMIT 100", conn)
    st.line_chart(df.set_index("date")["price_usd"])

elif menu == "SQL Runner":
    q = st.selectbox("Select Query", list(queries.keys()))

    if st.button("Run"):
        result = pd.read_sql(queries[q], conn)
        st.dataframe(result)