# Desafio 9: Realizar un análisis exploratorio de datos (EDA) básico con Pandas.

import pandas as pd

datos = {
    'edad': [25, 34, 45, 23, 35, 40, 29, 31, 50, 28],
    'ingresos': [30000, 50000, 70000, 25000, 60000, 80000, 40000, 45000, 90000, 35000],
    'gastos': [20000, 30000, 40000, 15000, 35000, 45000, 25000, 27000, 50000, 22000]
}   

df = pd.DataFrame(datos)
print("Primeras filas del DataFrame:")
print(df.head())

print("\nÚltimas filas del DataFrame:")
print(df.tail())

print("\nDescripción estadística del DataFrame:")
print(df.describe())

print("\nInformación del DataFrame:")
print(df.info())

print("\nCorrelación entre variables:")
print(df.corr())

# Explicación: Este desafío te introduce al análisis exploratorio de datos (EDA) utilizando Pandas. Aprenderás a obtener una visión general de un conjunto de datos mediante la visualización de las primeras filas, estadísticas descriptivas, información del DataFrame y análisis de correlación entre variables.
