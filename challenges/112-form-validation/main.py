# Desafio 112: Hacer una pagina web con un formulario que reciba el nombre del usuario y lo salude

from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def saludo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return f"<h1>¡Hola, {nombre}!</h1><p>Bienvenido a nuestra página web.</p>"
    return '''
        <form method="post">
            Nombre: <input type="text" name="nombre">
            <input type="submit" value="Enviar">
        </form>
    '''
    
if __name__ == '__main__':
    app.run(debug=True)
    
# Explicación: Usamos Flask para crear una página web con un formulario. Cuando el usuario envía su nombre, la aplicación lo saluda mostrando un mensaje personalizado. La ruta '/' maneja tanto solicitudes GET (mostrar el formulario) como POST (procesar el formulario).