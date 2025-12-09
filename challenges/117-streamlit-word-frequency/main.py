# Desafio 117: Hacer una pagina que reciba un texto y cuente la frecuencia de cada palabra con streamlit

import streamlit as st

st.title("Contador de Frecuencia de Palabras")
texto = st.text_area("Ingresa el texto aquí:")

if st.button("Contar Palabras"):

    texto = texto.lower().replace('.', '').replace(',', '')
    palabras = texto.split()
    
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
            
    st.write("Frecuencia de Palabras:")
    for palabra, frecuencia in frecuencia_palabras.items():
        st.write(f"{palabra}: {frecuencia}")
        
# Explicación: La aplicación de Streamlit recibe un texto del usuario, procesa el texto para contar la frecuencia de cada palabra y muestra los resultados en la página cuando el usuario hace clic en el botón "Contar Palabras".

# Texto de ejemplo:
# Python es un lenguaje de programación. Python es popular y versátil. Python es fácil de aprender. Python es divertido.
