# Desafío 43: Función recursiva para calcular el factorial

# 1 x 2 x 3 x ... x n-1 x n

# factorial(0) = 1
# factorial(1) = 1

# Explicación:
# La función se llama a sí misma con n-1 hasta llegar a 1, multiplicando en el camino.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial de 5 =", factorial(5))  # 120
