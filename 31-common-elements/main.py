# Desafío 31: Mostrá los elementos comunes entre dos listas
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
# Convertimos ambas listas a conjuntos (set) y usamos la intersección (&) para encontrar elementos comunes.
# Luego los convertimos de nuevo a lista.
print(list(set(a) & set(b)))
