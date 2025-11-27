# Desafío 53: Calendario que marca la fecha de hoy
# Explicación:
# Usamos el módulo 'calendar' para mostrar el mes actual y resaltamos el día de hoy
# con una simple marca manual.
import calendar
from datetime import datetime

def calendario_hoy():
    hoy = datetime.now()
    año = hoy.year
    mes = hoy.month
    dia = hoy.day

    cal = calendar.month(año, mes)

    # Pintar el día con ANSI escape codes (rojo)
    cal_coloreado = cal.replace(f"{dia:2}", f"\033[91m{dia:2}\033[0m")

    print("Calendario del mes actual:\n")
    print(cal_coloreado)
    print(f"Hoy es: {dia}/{mes}/{año}")

calendario_hoy()
