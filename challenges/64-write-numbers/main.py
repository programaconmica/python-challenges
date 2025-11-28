# Desafio 64: Escribir los numeros del 1 al N en un archivo

N = 10
with open("numeros.txt", "w") as archivo:
    for i in range(1, N + 1):
        archivo.write(f"{i}\n")

print(f"Se escribieron {N} números en numeros.txt")

# Explicación: Este código abre un archivo y escribe los números del 1 al N, cada uno en una nueva línea.
