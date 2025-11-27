# Desafio 97: Graficar la funcion coseno con matplotlib

# pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion():
    x = np.linspace(-10, 10, 400)
    y = np.cos(x)  # Puedes cambiar esta función a cualquier otra

    plt.plot(x, y)
    plt.title("Gráfica de la función coseno")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.show()
    
graficar_funcion() 

# Explicación: Usamos numpy para generar valores x y calcular sus cosenos. 
# Luego, usamos matplotlib para graficar la función coseno.
