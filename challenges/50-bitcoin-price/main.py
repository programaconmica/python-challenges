# Desafío 50: Llamar a una API para obtener el precio de bitcoin

# pip install requests

import requests

try:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur,ars"
    response = requests.get(url, timeout=5)
    data = response.json()
    btc_usd = data["bitcoin"]["usd"]

    print(f"Precio Bitcoin:")
    print(f" - USD: ${btc_usd}")
except Exception as e:
    print("No se pudo obtener el precio del Bitcoin. Error:", e)
