import sqlite3
import pandas as pd

conn = sqlite3.connect("db/database.db")

# Load CSV
crypto = pd.read_csv("data/crypto.csv")
crypto_prices = pd.read_csv("data/crypto_prices.csv")
oil = pd.read_csv("data/oil.csv")
stocks = pd.read_csv("data/stocks.csv")

# Insert into DB
crypto.to_sql("cryptocurrencies", conn, if_exists="replace", index=False)
crypto_prices.to_sql("crypto_prices", conn, if_exists="replace", index=False)
oil.to_sql("oil_prices", conn, if_exists="replace", index=False)
stocks.to_sql("stock_prices", conn, if_exists="replace", index=False)

conn.close()

print("✅ Database Created")