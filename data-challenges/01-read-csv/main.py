# Desafio 1: Leer un archivo CSV e imprimir su contenido

import pandas as pd

df = pd.read_csv('datos.csv') # lee csv en un data frame

print(df)
print(df.to_string()) # imprime todo el contenido del data frame (sino se imprime solo las primeras y ultimas 5 filas)

# Explicación: Este desafío te introduce a la biblioteca Pandas, que es esencial para la manipulación y análisis de datos en Python. Aprenderás a leer archivos CSV y a trabajar con DataFrames, que son estructuras de datos tabulares similares a las hojas de cálculo.
