# Desafia 71: Hacer una funcion para obtener el pronóstico del tiempo de una ciudad

import requests

def obtener_pronostico(ciudad):
    url = f"https://wttr.in/{ciudad}?lang=es"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Pronóstico para {ciudad}:")
            print(response.text)
        else:
            print("No se pudo obtener el pronóstico.")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso
# obtener_pronostico("Montevideo")
# Explicación: Usamos la API de wttr.in para obtener el pronóstico del tiempo en formato texto para una ciudad dada.
