# Desafio 107: Obtener la fecha y hora actual en la zona horaria local

from datetime import datetime

def fecha_hora_local():
    return datetime.now()

# Ejemplo de uso
print(fecha_hora_local())

# Explicación: Usamos datetime.now() para obtener la fecha y hora actual en la zona horaria local del sistema donde se ejecuta el código.
