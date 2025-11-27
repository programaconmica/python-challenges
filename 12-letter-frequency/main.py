# Desafío 12: Crear un diccionario con letras y su cantidad en un texto

texto = "banana"
frecuencias = {}

for letra in texto:
    frecuencias[letra] = frecuencias.get(letra, 0) + 1

print(frecuencias)

# Explicación: Contamos cuántas veces aparece cada letra usando un diccionario.
