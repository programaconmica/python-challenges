# Desafio 70: Crear un programa que lea un archivo CSV y muestre su contenido

import csv

def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
            lector = csv.reader(csvfile)
            for fila in lector:
                print(fila)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
            
# leer_csv('datos.csv')  # Asegúrate de tener un archivo datos.csv en el mismo directorio

# Explicación: Usa el módulo csv para leer un archivo CSV y mostrar cada fila como una lista.
