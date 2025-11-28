# Desafio 84: Funcion que cuente la cantidad de palabras en una frase

def contador_palabras():
    texto = input("Escribe una frase: ")
    palabras = texto.split()
    print(f"Tu frase tiene {len(palabras)} palabras.")

contador_palabras()

# Explicación: La función toma una frase del usuario, la divide en palabras usando split() y cuenta cuántas palabras hay con len().
