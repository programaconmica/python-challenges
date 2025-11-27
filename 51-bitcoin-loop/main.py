# Desafío 51: Obtener el precio del Bitcoin cada 5 segundos
# Explicación:
# Usamos la API pública de CoinGecko para obtener el precio del Bitcoin en USD, EUR y ARS.
# Con un bucle infinito, pedimos el precio cada 5 segundos y lo mostramos.
# Usamos try/except para manejar cualquier error de red sin que el programa se caiga.

import requests
import time

def precio_bitcoin_cada_5s():
    while True:
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur,ars"
            response = requests.get(url, timeout=5)
            data = response.json()
            btc_usd = data["bitcoin"]["usd"]

            print(f"Precio Bitcoin: ${btc_usd}")
            print("-" * 30)
        except Exception as e:
            print(e)

        time.sleep(5)  # Espera 5 segundos antes de volver a consultar

# precio_bitcoin_cada_5s()  # descomenta para ejecutar
