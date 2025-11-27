# Desafío 33: Mostrá el cuadrado de los números impares del 1 al 10
# Filtramos los impares con x % 2 != 0 y elevamos al cuadrado con x**2.
print([x**2 for x in range(1, 11) if x % 2 != 0])
