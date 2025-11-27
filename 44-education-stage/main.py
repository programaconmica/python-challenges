# Desafío 44: Función que pide edad y determina etapa educativa
# Explicación:
# Según el número ingresado, imprime si la persona está en escuela (<12), liceo (<18) o universidad.

def etapa_educativa():
    edad = int(input("¿Cuál es tu edad? "))
    if edad < 12:
        print("Estás en la escuela.")
    elif edad < 18:
        print("Estás en el liceo.")
    else:
        print("Estás en la universidad o trabajando.")

# etapa_educativa()  # descomenta para ejecutar
