# Desafio 104: Prueba de reaccion

import time
import random

print("Cuando veas 'YA!', presioná Enter lo más rápido posible...")
time.sleep(random.uniform(2, 5))  # Espera aleatoria entre 2 y 5 segundos
print("YA!")
inicio = time.time()
input()
fin = time.time()

reaccion = fin - inicio
print(f"Tu tiempo de reacción fue de {reaccion:.3f} segundos.")

# Explicación: El programa espera un tiempo aleatorio antes de mostrar "YA!". 
# Luego mide el tiempo que tarda el usuario en presionar Enter, calculando su tiempo de reacción.
