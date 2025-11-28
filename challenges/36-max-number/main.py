# Desafío 36: Encontrá el mayor de tres números
a = 10
b = 20
c = 30
print(max(a, b, c))

lista = [a, b, c]
mayor = lista[0]
for num in lista:
    if num > mayor:
        mayor = num
        
print(mayor)
# Explicación: La función max() devuelve el mayor de los tres números.
