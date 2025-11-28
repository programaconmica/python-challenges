# Desafio 99: Capturar una excepcion en una funcion con python

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except Exception as e:
        return f"Error inesperado: {e}"
    
print(dividir(10, 2))  # Salida: 5.0
print(dividir(10, 0))  # Salida: Error: No se puede dividir entre cero.

# Explicación: La función dividir intenta realizar una división y captura la excepción 
# ZeroDivisionError si el divisor es cero, devolviendo un mensaje de error en lugar 
# de interrumpir el programa.
