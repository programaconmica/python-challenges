# Desafio 115: Hacer una pagina en python con streamlit que muestre un grafico de barras

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico de Barras con Streamlit")

# Datos de ejemplo
data = {'Categoría': ['A', 'B', 'C', 'D'], 'Valores': [10, 20, 15, 25]}
df = pd.DataFrame(data)

# Crear gráfico de barras
fig, ax = plt.subplots()

ax.bar(df['Categoría'], df['Valores'], color='skyblue')
ax.set_xlabel('Categoría')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de Barras de Ejemplo')

st.pyplot(fig)

# Explicación: Usamos Streamlit para crear una aplicación web que muestra un gráfico de barras. Los datos se almacenan en un DataFrame de pandas y se utiliza matplotlib para crear el gráfico, que luego se muestra en la aplicación con st.pyplot().

# Para correr la aplicacion, guarda el codigo en un archivo main.py y ejecuta:
# streamlit run main.py

# Instala Streamlit si no lo tienes:
# pip install streamlit
# pip install pandas matplotlib
