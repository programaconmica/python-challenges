# Desafio 87: Piedra papel o tijera con python

import random

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)
    jugador = input("Elige piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("Opción inválida. Intenta de nuevo.")
        return

    print(f"Computadora eligió: {computadora}")

    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

# piedra_papel_tijera()  # descomenta para ejecutar

# Explicación: El jugador elige entre piedra, papel o tijera, y la computadora elige aleatoriamente.
# Se comparan las elecciones para determinar el ganador según las reglas del juego.
