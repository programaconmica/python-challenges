# Desafío 23: Contar cuántos dígitos tiene un número
n = 12345
print(len(str(n)))

# Explicación: Convertimos el número a string y luego su longitud.

longitud = 0
for d in str(n):
    longitud += 1
print(longitud)
