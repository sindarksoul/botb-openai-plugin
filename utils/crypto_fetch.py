import requests

def get_crypto_price(symbol: str):
    try:
        url = f"https://api.coincap.io/v2/assets/{symbol.lower()}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "BOTB-Plugin/1.0"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"External API error: {response.status_code}"}

        data = response.json()
        price = data["data"]["priceUsd"]

        return {
            "symbol": symbol.upper(),
            "price_usd": float(price)
        }

    except Exception as e:
        return {"error": f"Internal exception: {str(e)}"}
