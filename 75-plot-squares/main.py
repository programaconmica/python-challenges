# Desafio 75: Hacer una grafica con matplotlib que grafique una funcion de numeros cuadrados

# pip install matplotlib

import matplotlib.pyplot as plt

def graficar_cuadrados():
    numeros = list(range(1, 11))
    cuadrados = [n**2 for n in numeros]

    plt.plot(numeros, cuadrados, marker="o")
    plt.title("Cuadrados de los primeros 10 números")
    plt.xlabel("Número")
    plt.ylabel("Número al cuadrado")
    plt.grid(True)
    plt.show()

graficar_cuadrados()

# Explicación: Usamos matplotlib para graficar los números del 1 al 10 en el eje X y sus cuadrados en el eje Y, mostrando puntos con marcadores.
