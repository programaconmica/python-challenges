# Desafio 78: Secuencia de Fibonacci

def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia[:n]

N = 10
print(f"Los primeros {N} números de Fibonacci son: {fibonacci(N)}")

# Explicación: La función genera la secuencia de Fibonacci sumando los dos últimos números 
# para obtener el siguiente, hasta alcanzar la cantidad deseada.
