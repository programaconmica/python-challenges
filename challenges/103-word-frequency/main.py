# Desafio 103: Contar la frecuencia de cada palabra en un texto

texto = "Python es un lenguaje de programacion. Es un lenguaje muy popular y versatil para el desarrollo de software."

texto = texto.lower()

texto = texto.replace('.', '').replace(',', '')

palabras = texto.split()

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print(frecuencia_palabras)

# Explicación: Este desafío es un ejercicio de procesamiento de texto básico que utiliza 
# estructuras de datos fundamentales de Python, como los diccionarios. Es una habilidad esencial en el análisis de texto y la preparación de datos para tareas más complejas.
