# Desafio 119: Calculadora de IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = input('Ingresa tu peso en kilogramos:')
altura = input('Ingresa tu altura en metros:')

icm = calcular_imc(peso, altura)
print(f'Tu IMC es: {icm:.2f}')

# Explicación: La función calcular_imc toma el peso en kilogramos y la altura en metros para calcular el Índice de Masa Corporal (IMC) usando la fórmula IMC = peso / (altura^2). Luego, se solicita al usuario que ingrese su peso y altura, y se muestra el resultado formateado a dos decimales.
