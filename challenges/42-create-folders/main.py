# Desafío 42: Generar 1000 carpetas
# Explicación:
# Usamos os.makedirs en un bucle para crear carpetas llamadas carpeta_1, carpeta_2, ..., carpeta_1000.
import os

def crear_carpetas():
    for i in range(1, 1001):
        os.makedirs(f"carpeta_{i}", exist_ok=True)
    print("Se generaron 1000 carpetas")

# Recorre del 1 al 1000 intentando borrar cada carpeta llamada carpeta_i.
# Usa os.rmdir, que solo borra si la carpeta está vacía.

def borrar_carpetas():
    for i in range(1, 1001):
        nombre = f"carpeta_{i}"
        try:
            os.rmdir(nombre)
        except OSError:
            pass
    print("Se borraron 1000 carpetas")

# crear_carpetas()  # descomenta para ejecutar
# borrar_carpetas()  # descomenta para ejecutar
