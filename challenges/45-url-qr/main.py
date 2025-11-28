# Desafío 45: Transformar URL a código QR
# Explicación:
# Usamos la librería qrcode para generar el código QR de una URL y guardarlo como imagen.

# pip install pillow qrcode

import qrcode

def generar_qr(url, nombre_archivo="codigo_qr.png"):
    img = qrcode.make(url)
    img.save(nombre_archivo)
    print(f"Código QR guardado como {nombre_archivo}")

# Ejemplo de uso
generar_qr("https://www.python.org")
