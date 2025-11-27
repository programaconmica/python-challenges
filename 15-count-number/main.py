# Desafío 15: Contar cuántas veces aparece el numero 2 en una lista
numeros = [1, 2, 3, 2, 4, 2]
print(numeros.count(2))

cant_dos = 0
for x in numeros:
    if x == 2:
        cant_dos += 1
print(cant_dos)
# Explicación: El método count cuenta cuántas veces aparece un valor específico.
