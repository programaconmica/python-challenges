# Desafio 96: Hacer un programa que convierta un numero romano a decimal

romano = input("Ingresa un número romano: ").upper()
valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0
prev_valor = 0

for letra in reversed(romano):
    valor = valores[letra]
    if valor < prev_valor:
        total -= valor
    else:
        total += valor
    prev_valor = valor

print(total)  # Ejemplo: XXVII = 27

# Explicación: La función convierte un número romano a decimal sumando o restando valores 
# según las reglas de los números romanos. Las reglas indican que si un símbolo de menor 
# valor precede a uno de mayor valor, se resta; de lo contrario, se suma.
