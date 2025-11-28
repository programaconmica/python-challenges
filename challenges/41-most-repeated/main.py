# Desafío 41: Función que encuentre el número más repetido en una lista
from collections import Counter

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
contador = Counter(numeros)
mas_repetido = contador.most_common(1)[0][0]
print(mas_repetido)

# Explicación:
# Usamos Counter de collections para contar cuántas veces aparece cada elemento.
# most_common(1) devuelve el elemento más repetido y su cantidad en una tupla.
# [0][0] extrae solo el número más repetido.
