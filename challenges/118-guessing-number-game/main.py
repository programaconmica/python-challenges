# Desafio 118: Juego de adivinar el numero

import random

def juego_adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    while True:
        intento = input("Ingresa tu intento (o 'salir' para terminar): ")
        if intento.lower() == 'salir':
            print(f"El número secreto era {numero_secreto}. ¡Gracias por jugar!")
            break
        try:
            intento = int(intento)
            intentos += 1
            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Explicación: El juego genera un número secreto entre 1 y 100. El usuario intenta adivinar el número, recibiendo pistas si su intento es demasiado alto o bajo. El juego continúa hasta que el usuario adivina el número o decide salir.
