# Desafio 5: Agregar datos en un dataframe de Pandas.

import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [28, 34, 29, 22],
    'Equipo': ['Real Madrid', 'Barcelona', 'Valencia', 'Atletico Madrid']
}

df = pd.DataFrame(data)
print(df)

# agregar una nueva columna 'Partidos'
df['Partidos'] = [30, 40, 350, 28]
print(df)

# agregar filas
nueva_fila = pd.DataFrame({'Nombre': ['Jorge'], 'Edad': [30], 'Equipo': ['Sevilla'], 'Partidos': [320]})
df = pd.concat([df, nueva_fila], ignore_index=True)
print(df)

# Explicación: Este desafío te enseña cómo agregar nuevas columnas y filas a un DataFrame de Pandas. Estas operaciones son esenciales para la manipulación de datos y la preparación de conjuntos de datos para análisis posteriores.
