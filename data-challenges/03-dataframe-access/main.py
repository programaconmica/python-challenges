# Desafio 3: Acceder a elementos específicos en un dataframe de Pandas.

import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [28, 34, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)

print(df)

print(df.loc[1])  # Accede a la fila con índice 1 (Luis)
print(df['Nombre'])  # Accede a la columna 'Nombre'
print(df.at[2, 'Ciudad'])  # Accede al elemento en la fila 2, columna 'Ciudad'

# Explicación: Este desafío te enseña cómo acceder a datos específicos dentro de un DataFrame de Pandas utilizando diferentes métodos como loc, iloc y at. Estas habilidades son fundamentales para manipular y analizar datos de manera efectiva.
