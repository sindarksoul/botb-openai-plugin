import requests

def get_crypto_price(symbol: str):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (compatible; BOTB-Plugin/1.0; +https://botb-openai-plugin.onrender.com)"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"External API error: {response.status_code}"}

        data = response.json()

        if symbol.lower() not in data:
            return {"error": f"Symbol '{symbol}' not found in API response."}

        return {
            "symbol": symbol.upper(),
            "price_usd": data[symbol.lower()]["usd"]
        }

    except Exception as e:
        return {"error": f"Internal exception: {str(e)}"}
