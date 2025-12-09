# Desafio 100: Usar la clausula else en un bloque try except

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else: # ejecuta si no hubo excepcion
        print("Archivo leído exitosamente:")
        print(contenido)
    finally: # se ejecuta siempre al final
        print("Operación de lectura de archivo finalizada.")
        
# leer_archivo("archivo.txt")  # descomenta para ejecutar

# Explicación: La función intenta leer un archivo y maneja posibles excepciones. 
# Si no hay excepciones, el bloque else se ejecuta mostrando el contenido del archivo. 
# El bloque finally se ejecuta siempre al final, independientemente de si hubo una excepción o no.
