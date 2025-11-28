# Desafio 95: Verificar si un numero es perfecto

def es_perfecto(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print(es_perfecto(28))  # True, ejemplo: 28 es un número perfecto

# Explicación: Un número perfecto es igual a la suma de sus divisores propios. 
# La función verifica esto sumando los divisores y comparándolos con el número original.
# 28 = 1 + 2 + 4 + 7 + 14
