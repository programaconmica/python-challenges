# Desafío 6: En una sola línea mostrá solo los números pares de una lista

lista = [1, 2, 3, 4, 5, 6, 7, 8]

print([x for x in lista if x % 2 == 0])

# Usamos comprensión de listas con un condicional para incluir solo los números que sean pares (x % 2 == 0).