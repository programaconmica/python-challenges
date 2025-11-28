# Desafío 22: Que imprime esto?

csl1 = l2 = []
l1.append(1)
l2.append(2)
print(l1, l2)

# Resultado: [1, 2] [1, 2]
# Explicación: 
# l1 = l2 = [] hace que l1 y l2 apunten al mismo objeto en memoria, es decir, a la misma lista vacía. 
# No estás creando dos listas diferentes, sino una sola lista referenciada por dos nombres distintos (l1 y l2).
# l1.append(1) agrega un 1 a la lista, l2.append(2) agrega un 2 a la lista y por eso se imprime el resultado
# para hacer listas distintas usa l1 = []   l2 = [] o l2 = l1.copy()
