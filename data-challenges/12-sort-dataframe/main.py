# Desafio 12: Ordenar un dataframe de Pandas por una o más columnas.

import pandas as pd

datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [28, 34, 29, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid']
}

df = pd.DataFrame(datos)
print("Datos originales:")
print(df)

# Ordenar por 'Edad' de forma ascendente
df_ordenado_edad = df.sort_values(by='Edad')
print("\nDatos ordenados por Edad (ascendente):")
print(df_ordenado_edad)

# Ordenar por 'Ciudad' de forma descendente y luego por 'Edad' ascendente
df_ordenado_ciudad_edad = df.sort_values(by=['Ciudad', 'Edad'], ascending=[False, True])
print("\nDatos ordenados por Ciudad (descendente) y Edad (ascendente):")
print(df_ordenado_ciudad_edad)

# Explicación: Este desafío te enseña cómo ordenar un DataFrame de Pandas por una o más columnas utilizando el método sort_values. Aprenderás a especificar el orden (ascendente o descendente) para cada columna, lo cual es útil para organizar y analizar datos de manera efectiva.
