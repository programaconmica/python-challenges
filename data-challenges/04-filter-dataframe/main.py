# Desafio 4: Filtrar datos en un dataframe de Pandas.

import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [28, 34, 29, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid']
}

df = pd.DataFrame(data)
print(df)

filtro = df['Ciudad'] == 'Madrid'
df_filtrado = df[filtro]
print(df_filtrado)

# Explicación: Este desafío te muestra cómo filtrar filas en un DataFrame de Pandas basándote en condiciones específicas. Aprenderás a crear filtros booleanos y a aplicarlos para extraer subconjuntos de datos relevantes.
