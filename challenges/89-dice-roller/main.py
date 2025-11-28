# Desafio 89: Simular un dado

import random

def lanzar_dado():
    return random.randint(1, 6)

print(f"Lanzando el dado... Salió un: {lanzar_dado()}")

# Explicación: La función lanzar_dado genera un número aleatorio entre 1 y 6, simulando el lanzamiento de un dado.
