# Desafío 48: Imprimir tabla de multiplicación
# Explicación:
# Pide un número al usuario, imprime su tabla del 1 al 10,
# y la guarda en un archivo llamado tablaN.txt (por ejemplo tabla7.txt si el número es 7).

def tabla_multiplicar():
    N = int(input("Ingrese un número para la tabla: "))
    nombre_archivo = f"tabla{N}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Tabla del {N}\n")
        archivo.write("-" * 20 + "\n")
        for i in range(1, 11):
            linea = f"{N} x {i} = {N * i}"
            archivo.write(linea + "\n")
    print(f"Tabla guardada en {nombre_archivo}")

# tabla_multiplicar()
