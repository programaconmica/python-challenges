# Desafio 102: Debugger una funcion con la ayuda de assert

def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero."
    return a / b

try:
    print(dividir(10, 2))  # Salida: 5.0
    print(dividir(10, 0))  # Esto lanzará una excepción
except AssertionError as e:
    print(f"Error: {e}")
    
# Explicación: La función dividir usa assert para verificar que el divisor no sea cero. 
# Si b es 0, se lanza una excepción AssertionError con un mensaje. 
# Usamos un bloque try-except para manejar la excepción y mostrar el mensaje de error.
