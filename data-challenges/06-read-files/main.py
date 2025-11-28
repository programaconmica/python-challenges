# Desafio 6: Leer distintos tipos de archivos con Pandas (CSV, Excel, JSON).

import pandas as pd

# Leer un archivo CSV
try:
    df_csv = pd.read_csv('datos.csv')
    print("Datos CSV:")
    print(df_csv)
except FileNotFoundError:
    print("Archivo datos.csv no encontrado")

# Leer un archivo Excel
try:
    df_excel = pd.read_excel('datos.xlsx')
    print("\nDatos Excel:")
    print(df_excel)
except FileNotFoundError:
    print("Archivo datos.xlsx no encontrado")

# Leer un archivo JSON
try:
    df_json = pd.read_json('datos.json')
    print("\nDatos JSON:")
    print(df_json)
except FileNotFoundError:
    print("Archivo datos.json no encontrado")

# Explicación: Este desafío te introduce a la capacidad de Pandas para leer diferentes formatos de archivos comunes en el análisis de datos, como CSV, Excel y JSON. Aprenderás a cargar datos desde estos formatos en DataFrames para su posterior manipulación y análisis.
