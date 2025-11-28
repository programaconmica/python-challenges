# Desafio 74: Juego donde el usuario tiene que adivinar un numero entre el 1 y el 100

import random

def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("Adivina el número entre 1 y 100")

    while True:
        intento = int(input("Tu intento: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo ⬇️")
        elif intento > numero_secreto:
            print("Demasiado alto ⬆️")
        else:
            print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos.")
            break

adivina_numero()

# Explicación: Generamos un número aleatorio entre 1 y 100. El usuario intenta adivinarlo y recibe pistas 
# si su intento es demasiado alto o bajo, hasta que acierta.
