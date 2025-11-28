# Desafío 81: Usar libreria numpy para hacer operaciones con matrices

# pip install numpy

import numpy as np

def operaciones_matrices():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matriz A:")
    print(A)
    print("\nMatriz B:")
    print(B)
    
    suma = A + B
    print("\nSuma de A y B:")
    print(suma)
    
    producto = np.dot(A, B)
    print("\nProducto de A y B:")
    print(producto)
    
    transpuesta_A = A.T
    print("\nTranspuesta de A:")
    print(transpuesta_A)
    
operaciones_matrices()
