# Desafío 49: Hacer ruleta rusa en Python
# Explicación:
# Simulamos una pistola con 6 cámaras. Generamos dos números aleatorios del 1 al 6.
# Si coinciden, dispara ("Bang!"), si no, solo hace click y se salva.
import random
import time

def ruleta_rusa():
    print("Girando el tambor...")
    time.sleep(2)
    bala = random.randint(1, 6)
    disparo = random.randint(1, 6)
    if bala == disparo:
        print("Bang! 💀 Perdiste...")
    else:
        print("Click... Te salvaste.")

ruleta_rusa()
