# Desafío 46: Consumir una API para generar chistes
# Explicación:
# Hacemos un GET a la API pública de Joke API para obtener chistes en español.

# pip install requests

import requests

try:
    response = requests.get("https://v2.jokeapi.dev/joke/Any?lang=es", timeout=5)
    data = response.json()
    
    print(data)

    if data["type"] == "single":
        print("Chiste:", data["joke"])
    else:
        print("Chiste:", data["setup"])
        print("Remate:", data["delivery"])
except Exception as e:
    print("No se pudo obtener un chiste. Error:", e)
