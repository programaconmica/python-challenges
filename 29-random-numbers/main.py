# Desafío 29: Generar 5 números aleatorios entre 1 y 100
import random

aleatorios = [random.randint(1, 100) for _ in range(5)]
print(aleatorios)

for _ in range(5):
    print(random.randint(1, 100))
# Explicación: randint genera un número entero aleatorio en un rango.
