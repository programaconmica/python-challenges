# Desafío 11: Contar cuántas palabras tienen más de 5 letras

frase = "Python es un lenguaje genial para programar"
palabras = frase.split()
contador = 0

for palabra in palabras:
    if len(palabra) > 5:
        contador += 1

print(contador)

# Explicación: Separamos la frase en palabras y contamos las que tienen más de 5 caracteres.
