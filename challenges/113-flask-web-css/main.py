# Desafio 113: Hacer una pagina web con python y estilos css

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')

def inicio():
    return render_template_string('''
    <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f0f0f0; text-align: center; }
                h1 { color: #333; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>¡Hola, Mundo!</h1>
            <p>Esta es una página web con estilos CSS simples.</p>
        </body>
    </html>
    ''')
    
if __name__ == '__main__':
    app.run(debug=True)
    
# Explicación: Usamos Flask para crear una página web que incluye estilos CSS directamente en la plantilla HTML. El bloque <style> dentro de la sección <head> define los estilos para el cuerpo, encabezados y párrafos de la página.
