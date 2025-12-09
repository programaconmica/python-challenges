# Desafio 116: Hacer una pagina en python con streamlit que reciba un numero y muestre su factorial

import streamlit as st
import math

st.title("Calculadora de Factorial")

numero = st.number_input("Ingresa un número entero:", min_value=0, step=1)

if st.button("Calcular Factorial"):
    resultado = math.factorial(numero)
    st.write(f"El factorial de {numero} es {resultado}")
    
# Correr la aplicación con: streamlit run main.py
    
# Explicación: Usamos Streamlit para crear una aplicación web que recibe un número entero del usuario y calcula su factorial usando la función math.factorial(). El resultado se muestra cuando el usuario hace clic en el botón "Calcular Factorial".
