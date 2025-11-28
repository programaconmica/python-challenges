# Desafio 7: Manejar datos faltantes en un dataframe de Pandas.

import pandas as pd
import numpy as np

datos = {
    'region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte'],
    'ventas': [200, np.nan, 150, np.nan, 300],
    'clientes': [20, 15, np.nan, 10, 25]
}

df = pd.DataFrame(datos)
print("Datos originales:")
print(df)

# Manejar datos faltantes
df['ventas'] = df['ventas'].fillna(df['ventas'].mean())  # Rellenar con la media
df['clientes'] = df['clientes'].fillna(method='ffill')  # Rellenar con el valor anterior
print("\nDatos después de manejar valores faltantes:")
print(df)

# Explicación: Este desafío te enseña cómo manejar datos faltantes en un DataFrame de Pandas, una tarea común en el análisis de datos. Aprenderás a identificar valores NaN y a utilizar diferentes técnicas para rellenarlos, como la media o el método de propagación hacia adelante (ffill).
