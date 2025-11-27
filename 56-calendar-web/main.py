# Desafio 56: Hacer un calendario que se vea en la web

import calendar
from datetime import datetime
import webbrowser
import re  # Importamos el módulo de expresiones regulares

def calendario_hoy_html():
    hoy = datetime.now()
    año = hoy.year
    mes = hoy.month
    dia = hoy.day

    # Obtenemos el calendario del mes
    cal = calendar.month(año, mes)

    # Usamos una expresión regular para reemplazar solo el día exacto
    cal_html = re.sub(
        rf"(?<!\d){dia:2}(?!\d)",  # Coincide con el día exacto (no precedido ni seguido por dígitos)
        f"<span style='color:red;font-weight:bold;'>{dia:2}</span>",
        cal
    )

    # Generamos el HTML
    html = f"""
    <html>
    <head><title>Calendario</title></head>
    <body style='font-family: monospace; white-space: pre;'>
    {cal_html}
    <br>Hoy es: {dia}/{mes}/{año}
    </body>
    </html>
    """

    # Guardamos el HTML en un archivo y lo abrimos en el navegador
    with open("calendario.html", "w") as f:
        f.write(html)

    webbrowser.open("calendario.html")
    print("Calendario abierto en el navegador")

# calendario_hoy_html()  # descomenta para ejecutar
# Explicación: Generamos un archivo HTML y usamos expresiones regulares para resaltar el día actual sin afectar otros números.
