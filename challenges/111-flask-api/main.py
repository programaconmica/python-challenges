# Desafio 111: Hacer una pagina web simple con python

from flask import Flask

app = Flask(__name__)
@app.route('/')

def inicio():
    return "<h1>¡Hola, Mundo!</h1><p>Esta es una página web simple creada con Flask.</p>"

if __name__ == '__main__':
    app.run(debug=True)
    
# Explicación: Usamos Flask para crear una aplicación web simple que muestra un mensaje en la página de inicio. La función inicio() define el contenido que se muestra cuando se accede a la ruta raíz ('/').