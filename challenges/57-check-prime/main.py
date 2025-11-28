# Desafío 57: Verificar si un número es primo

num = 7
es_primo = True

if num < 2:
    es_primo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            es_primo = False
            break

print("¿Es primo?", es_primo)

# Explicación: Un número primo solo es divisible por 1 y por sí mismo. 
# Si un número tiene un divisor mayor que su raíz cuadrada, también tendrá un divisor menor que la raíz cuadrada
