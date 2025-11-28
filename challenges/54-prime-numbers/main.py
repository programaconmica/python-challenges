# Desafío 54: Mostrar los primeros N números primos
# Explicación:
# Pide al usuario cuántos primos mostrar y los imprime calculando con una función is_prime.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def mostrar_primos():
    N = int(input("¿Cuántos números primos querés ver? "))
    contador = 0
    numero = 2
    while contador < N:
        if es_primo(numero):
            print(numero, end=" ")
            contador += 1
        numero += 1
    print()

# mostrar_primos()
