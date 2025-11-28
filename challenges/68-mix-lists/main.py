# Desafio 68: Mezclar los elementos de dos listas

import random

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
mezclada = lista1 + lista2
random.shuffle(mezclada)
print(mezclada)

# Explicación: Une dos listas y luego las mezcla aleatoriamente con shuffle.
