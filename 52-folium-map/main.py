# Desafío 52: Generar un mapa 
# Explicación:
# Usamos la librería 'folium' para crear un mapa centrado en una ubicación dada
# y guardar el resultado como archivo HTML que se puede abrir en el navegador.

# pip install folium

import folium

def generar_mapa():
    latitud = -34.9011  # Montevideo
    longitud = -56.1645

    # Crear el mapa
    mapa = folium.Map(location=[latitud, longitud], zoom_start=13)

    # Agregar un marcador
    folium.Marker(
        location=[latitud, longitud],
        popup="Montevideo",
        tooltip="Click para info"
    ).add_to(mapa)

    # Guardar el mapa
    mapa.save("mapa.html")
    print("Mapa guardado como mapa.html")

generar_mapa()
