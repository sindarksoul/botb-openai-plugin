import requests

def get_crypto_price(symbol: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    res = requests.get(url)
    return res.json()
