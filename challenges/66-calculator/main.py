# Desafio 66: Hacer una calculadora basica en python

def calculadora():
    print("Calculadora Básica")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingresa el número de la operación (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción inválida. Por favor, selecciona una operación válida.")

# calculadora()  # descomenta para ejecutar

# Explicación:
# El programa muestra un menú con las operaciones básicas.
# El usuario selecciona una operación ingresando un número (1-4).
# Se solicitan dos números como entrada.
# Según la operación seleccionada, se realiza el cálculo y se muestra el resultado.
# Si el usuario intenta dividir entre 0, se muestra un mensaje de error.
