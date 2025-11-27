# Desafío 18: Generar una contraseña aleatoria
import random

caracteres = "abc123"

contrasena = ""

for _ in range(6):
    contrasena += random.choice(caracteres)

print(contrasena)

password = "".join(random.choice(caracteres) for _ in range(6))
print(password)
# Explicación: Usamos random.choice y join unir los caracteres para formar una cadena aleatoria.
