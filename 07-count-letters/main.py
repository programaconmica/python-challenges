# Desafío 7: Contá cuántas veces aparece cada letra

palabra = "banana"
conteo = {}
for letra in palabra:
    conteo[letra] = conteo.get(letra, 0) + 1
print(conteo)

# Recorremos cada letra y usamos el método get() del diccionario para obtener el valor actual o 0 si no existe.
# Luego sumamos uno. Esto nos permite contar las apariciones sin errores.