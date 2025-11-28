# Desafío 14: Verificar si una lista está ordenada de menor a mayor

lista = [1, 2, 3, 4, 5]
ordenada = True

for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break

print("¿Está ordenada?", ordenada)

# Explicación: Comparamos cada elemento con el siguiente para verificar que estén en orden creciente.
