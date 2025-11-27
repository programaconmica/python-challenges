# Desafio 94: Hacer un mapa en la web que sea abierto por un boton en tkinter

# pip install folium tkinter

import tkinter as tk
import folium
import webbrowser

def crear_mapa():
    # Crear un mapa centrado en una ubicación específica
    mapa = folium.Map(location=[-34.9011, -56.1645], zoom_start=13)
    # Guardar el mapa como archivo HTML
    mapa.save("mapa.html")
    # Abrir el mapa en el navegador web
    webbrowser.open("mapa.html")
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mapa con Folium")
ventana.geometry("300x200")
# Crear un botón que genera y muestra el mapa al hacer clic
boton = tk.Button(ventana, text="Mostrar Mapa", command=crear_mapa)
boton.pack(pady=20)
# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
