# Desafío 8: Eliminá duplicados sin perder el orden

lista = [1, 2, 2, 3, 1, 4]
res = []

[res.append(x) for x in lista if x not in res]
print(res)

# Recorremos la lista y solo agregamos los elementos que aún no están en la nueva lista.
# Esto elimina duplicados sin usar set, lo que preserva el orden.