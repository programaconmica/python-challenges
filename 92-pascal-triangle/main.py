# Desafio 92: Hacer el triangulo de pascal

def triangulo_pascal(niveles):
    triangulo = []
    for i in range(niveles):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        triangulo.append(fila)
    return triangulo

triangulo = triangulo_pascal(5)
for fila in triangulo:
    print(fila)
    
# Explicación: La función triangulo_pascal genera el triángulo de Pascal hasta el número de niveles especificado.
# Cada número en el triángulo es la suma de los dos números directamente arriba de él en la fila anterior.
