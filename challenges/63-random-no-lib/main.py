# Desafio 63: Función para obtener un numero random sin usar librerias

def random_number():
    number = id(object())
    last_digit = number % 10
    return last_digit

print("Random:", random_number())

import random
print("Con librería:", random.randint(0, 9))

# Explicación: La función random_number genera un número pseudoaleatorio entre 0 y 9 sin usar librerías externas. 
# Utiliza el identificador único de un nuevo objeto creado con id(object()) como semilla, que es un entero único 
# basado en la dirección de memoria del objeto. Luego, calcula el residuo de dividir este identificador entre 10 (% 10), 
# obteniendo el último dígito del número.
