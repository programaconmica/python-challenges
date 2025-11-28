# Desafio 93: Hacer una interfaz grafica simple con tkinter

# pip install tkinter (generalmente viene con Python)

import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Hola, Mundo!")
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica Simple")
ventana.geometry("300x200")
# Crear un botón que muestra un mensaje al hacer clic
boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack(pady=20)
# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
