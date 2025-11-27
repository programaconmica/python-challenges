# Desafío 32: Convertí una lista de listas en una sola lista
lista = [[1, 2], [3, 4], [5]]
# Usamos comprensión anidada para extraer cada elemento de las sublistas y formar una sola lista.
print([x for sub in lista for x in sub])
