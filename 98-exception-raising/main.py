# Desafio 98: Lanzar una excepcion en una funcion con python

def funcion_con_excepcion(x):
    if x < 0:
        raise ValueError("El valor no puede ser negativo.")
    return x

try:
    resultado = funcion_con_excepcion(-5)
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Error: {e}")
    
# Explicación: La función lanza una excepción ValueError si el argumento es negativo. 
# Usamos un bloque try-except para manejar la excepción y mostrar un mensaje de error 
# sin interrumpir el programa.
