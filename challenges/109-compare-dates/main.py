# Desafio 109: Comparar dos fechas con distintas zonas horarias

from datetime import datetime

def comparar_fechas(fecha1, fecha2):

    dt1 = datetime.fromisoformat(fecha1)
    dt2 = datetime.fromisoformat(fecha2)
    
    if dt1 < dt2:
        return f"{fecha1} es anterior a {fecha2}"
    elif dt1 > dt2:
        return f"{fecha1} es posterior a {fecha2}"
    else:
        return "Ambas fechas son iguales"
    
# Ejemplo de uso
fecha_a = "2024-06-15T10:00:00-03:00"  # Hora de Montevideo (UTC-3)
fecha_b = "2024-06-15T14:00:00+01:00"  # Hora de Londres (UTC+1)
resultado = comparar_fechas(fecha_a, fecha_b)
print(resultado)

# Explicación: La función comparar_fechas convierte las cadenas de fecha en objetos datetime con zona horaria usando fromisoformat(). Luego compara las fechas teniendo en cuenta las diferencias de zona horaria.
