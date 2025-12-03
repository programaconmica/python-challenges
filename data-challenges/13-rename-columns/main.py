# Desafio 13: Renombrar columnas en un dataframe de Pandas.

import pandas as pd

datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [28, 34, 29, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid']
}

df = pd.DataFrame(datos)
print("Datos originales:")
print(df)

# Renombrar columnas
df_renombrado = df.rename(columns={'Nombre': 'Nombre_Completo', 'Edad': 'Años', 'Ciudad': 'Localidad'})
print("\nDatos con columnas renombradas:")
print(df_renombrado)

# Explicación: Este desafío te muestra cómo renombrar columnas en un DataFrame de Pandas utilizando el método rename. Aprenderás a cambiar los nombres de las columnas para que sean más descriptivos o adecuados para tu análisis de datos.
