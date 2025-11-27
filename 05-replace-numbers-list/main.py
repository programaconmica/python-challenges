# Desafío 5: Reemplazar números negativos por 0 en una lista

numeros = [4, -3, 2, -1, 0]
for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print(numeros)

# Explicación: Recorremos la lista por índice y reemplazamos los valores negativos con 0.