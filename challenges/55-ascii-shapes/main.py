# Desafío 55: Dibujar un triángulo y un cuadrado con asteriscos
# Explicación:
# Pide un tamaño N y dibuja un triángulo rectángulo y un cuadrado con N filas.

def dibujar_triangulo():
    N = int(input("Ingresa el tamaño N para dibujar el triangulo: "))

    print("\nTriángulo:")
    for i in range(1, N+1):
        print("* " * i)

def dibujar_cuadrado():
    N = int(input("Ingresa el tamaño N para dibujar el cuadrado: "))

    print("\nCuadrado:")
    for i in range(N):
        print("* " * N)

# dibujar_cuadrado()
# dibujar_triangulo()
