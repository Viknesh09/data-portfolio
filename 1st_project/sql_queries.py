queries = {

    "Top 3 Crypto":
    "SELECT * FROM cryptocurrencies ORDER BY market_cap DESC LIMIT 3;",

    "Bitcoin Max Price":
    "SELECT MAX(price_usd) FROM crypto_prices WHERE coin_id='bitcoin';",

    "Oil Max Price":
    "SELECT MAX(price_usd) FROM oil_prices;"

}