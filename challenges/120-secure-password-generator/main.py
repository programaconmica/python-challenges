# Desafio 120: Generador de contraseñas seguras

import random

def generar_contrasena(longitud=12):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

contrasena = generar_contrasena(16)
print(f"Contraseña segura generada: {contrasena}")

# Explicación: La función generar_contrasena crea una contraseña aleatoria de una longitud especificada utilizando letras mayúsculas, minúsculas, números y caracteres especiales. La contraseña se genera seleccionando caracteres al azar de la cadena de caracteres permitidos.
