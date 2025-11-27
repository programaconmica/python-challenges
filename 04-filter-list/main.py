# Desafío 4: Filtrar palabras que empiecen con vocal

palabras = ["hola", "árbol", "idea", "sol", "universo"]
vocales = "aeiouáéíóú"

resultado = []
for palabra in palabras:
    if palabra[0].lower() in vocales:
        resultado.append(palabra)

print(resultado)

# Explicación: Recorremos cada palabra y si empieza con vocal (mayúscula o minúscula), la agregamos a la lista resultado.