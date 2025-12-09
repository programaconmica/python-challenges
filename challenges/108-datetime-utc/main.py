# Desafio 108: Obtener la fecha y hora actual en UTC

from datetime import datetime, timezone

def fecha_utc_now():
    return datetime.now(timezone.utc)

# Ejemplo de uso
print(fecha_utc_now())

# La misma funcion pero en formato ISO 8601:

def fecha_utc_iso():
    return datetime.now(timezone.utc).isoformat()

# Ejemplo de uso
print(fecha_utc_iso())

# Explicación: Usamos datetime.now() con timezone.utc para obtener la fecha y hora actual en UTC. 
# El método isoformat() devuelve la fecha y hora en formato ISO 8601.
