# Desafio 11: Eliminar filas con valores nulos en un dataframe de Pandas.

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

# Eliminar filas con valores nulos
df_limpio = df.dropna() 
# Elimina filas con cualquier valor NaN y crea un nuevo DataFrame. 
# Para modificar el DataFrame original, usar df.dropna(inplace=True)
print("\nDatos después de eliminar filas con valores nulos:")
print(df_limpio)

# Explicación: Este desafío te muestra cómo eliminar filas con valores nulos en un DataFrame de Pandas. Aprenderás a usar el método dropna para limpiar tus datos, lo cual es crucial para asegurar la calidad y precisión del análisis de datos.
