# Desafío 20: Sumá todos los dígitos de un número

n = 12345
print(sum(int(d) for d in str(n)))

suma = 0
for d in str(n):
    suma += int(d)
print(suma)

# Convertimos el número a string para recorrer sus dígitos, los convertimos a int y usamos sum().