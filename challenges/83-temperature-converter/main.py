# Desafio 83: Funcion que convierta de Fahrenheit a Celsius y viceversa

def conversor_temperaturas():
    print("🌡️ Conversor de Temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción (1/2): ")

    if opcion == "1":
        c = float(input("Ingresa la temperatura en °C: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif opcion == "2":
        f = float(input("Ingresa la temperatura en °F: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Opción inválida")

conversor_temperaturas()

# Explicación: La función pide al usuario elegir entre convertir de Celsius a Fahrenheit o viceversa,
# luego realiza la conversión y muestra el resultado.
