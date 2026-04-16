import requests
import pandas as pd
import yfinance as yf

# -------------------------------
# CRYPTO DATA
# -------------------------------
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}

    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data)

    df = df[["id", "symbol", "name", "current_price", "market_cap",
             "market_cap_rank", "total_volume", "circulating_supply",
             "total_supply", "ath", "atl", "last_updated"]]

    df["date"] = pd.to_datetime(df["last_updated"]).dt.date
    df.drop(columns=["last_updated"], inplace=True)

    df.to_csv("data/crypto.csv", index=False)
    return df


# -------------------------------
# CRYPTO PRICES
# -------------------------------
def get_crypto_prices(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": 365}

    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data["prices"], columns=["timestamp", "price_usd"])

    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df["coin_id"] = coin

    return df[["coin_id", "date", "price_usd"]]


# -------------------------------
# OIL DATA
# -------------------------------
def get_oil_data():
    url = "https://raw.githubusercontent.com/datasets/oil-prices/main/data/wti-daily.csv"
    df = pd.read_csv(url)

    df.columns = ["date", "price_usd"]
    df.to_csv("data/oil.csv", index=False)

    return df


# -------------------------------
# STOCK DATA
# -------------------------------
def get_stock_data():
    tickers = ["^GSPC", "^IXIC", "^NSEI"]
    all_data = []

    for ticker in tickers:
        df = yf.download(ticker, start="2020-01-01", end="2025-09-30")
        df.reset_index(inplace=True)

        df["ticker"] = ticker
        all_data.append(df)

    final_df = pd.concat(all_data)
    final_df.to_csv("data/stocks.csv", index=False)

    return final_df


# -------------------------------
# RUN ALL
# -------------------------------
if __name__ == "__main__":
    crypto = get_crypto_data()

    top3 = crypto.nsmallest(3, "market_cap_rank")["id"].tolist()
    prices = pd.concat([get_crypto_prices(c) for c in top3])

    prices.to_csv("data/crypto_prices.csv", index=False)

    get_oil_data()
    get_stock_data()

    print("✅ Data Collection Done")