# Desafio 65: Escribir el cuadrado de los numeros del 1 al N en un archivo

N = 10
with open("cuadrados.txt", "w") as archivo:
    for i in range(1, N + 1):
        archivo.write(f"numero: {i} - cuadrado: {i**2}\n")

print(f"Se escribieron cuadrados en cuadrados.txt")

# Explicación: Este código abre un archivo y escribe el cuadrado de los números del 1 al N, cada uno en una nueva línea.
