# Desafío 47: Reloj que se actualiza cada 1 segundo
# Explicación:
# Usamos time.strftime para mostrar la hora y time.sleep(1) para actualizar cada segundo.
# end="\r" sobrescribe la línea anterior, simulando un reloj en tiempo real.
import time

def reloj():
    try:
        while True:
            print(time.strftime("%H:%M:%S"), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReloj detenido.")

# reloj()  # descomenta para ejecutar
