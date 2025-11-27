# Desafío 9: En una sola linea mostrá la palabra más larga

palabras = ["casa", "ventana", "auto", "computadora"]
print(max(palabras, key=len))

# Usamos la función max() con key=len para encontrar la palabra con mayor cantidad de letras.
# La función len() devuelve la longitud de un string.