# Desafio 114: Hacer una pagina web con python que muestre una imagen

from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')

def inicio():
    return render_template_string('''
    <html>
        <head>
            <title>Página con Imagen</title>
        </head>
        <body>
            <h1>¡Hola, Mundo!</h1>
            <p>Esta es una página web que muestra una imagen.</p>
            <img src="{{ url_for('static', filename='imagen.jpg') }}" alt="Imagen de ejemplo" width="300">
        </body>
    </html>
    ''')
    
if __name__ == '__main__':
    app.run(debug=True)
    
# Explicación: Usamos Flask para crear una página web que muestra una imagen almacenada en la carpeta 'static'. La función url_for genera la URL correcta para acceder a la imagen. Asegúrate de tener una imagen llamada 'imagen.jpg' en la carpeta 'static' dentro del directorio de tu aplicación Flask.
