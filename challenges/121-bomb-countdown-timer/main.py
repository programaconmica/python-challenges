# Desafio 121: Temporizador de cuenta regresiva con bomba que explota

import time

def temporizador_bomba(segundos):
    print("Temporizador iniciado...")
    while segundos:
        mins = segundos // 60
        secs = segundos % 60
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1
    print("¡BOOM! La bomba ha explotado.")

temporizador_bomba(10)

# Explicación: La función temporizador_bomba inicia una cuenta regresiva desde el número de segundos especificado. Muestra el tiempo restante en formato MM:SS y, cuando llega a cero, imprime un mensaje indicando que la bomba ha explotado.
