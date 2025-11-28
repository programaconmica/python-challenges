# Desafio 8: Realizar operaciones de agrupamiento y agregación en un dataframe de Pandas.

import pandas as pd

datos = {
    'region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur'],
    'ventas': [200, 150, 300, 250, 400, 100],
    'clientes': [20, 15, 30, 25, 40, 10]
}   

df = pd.DataFrame(datos)
print("Datos originales:")
print(df)

# Agrupar por 'region' y calcular la suma de 'ventas' y 'clientes'
agrupado = df.groupby('region').agg({'ventas': 'sum', 'clientes': 'sum'})
print("\nDatos agrupados por región:")
print(agrupado)

# Explicación: Este desafío te muestra cómo realizar operaciones de agrupamiento y agregación en un DataFrame de Pandas. Aprenderás a usar el método groupby para agrupar datos por una o más columnas y a aplicar funciones de agregación como sum, mean, etc., para obtener resúmenes útiles de los datos.
