# Desafío 80: Usar la libreria pandas para analizar datos de un archivo CSV

# pip install pandas

import pandas as pd

def analizar_csv(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    print("Primeras 5 filas del DataFrame:")
    print(df.head())
    print("\nDescripción estadística:")
    print(df.describe())
    print("\nInformación del DataFrame:")
    print(df.info())
    
analizar_csv('datos.csv')  # Asegúrate de tener un archivo datos.csv
