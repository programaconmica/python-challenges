# Desafío 39: Encontrá el promedio de una lista de números
nums = [10, 20, 30, 40]
print(sum(nums) / len(nums))
# Explicación: sum() suma todos los números y len() cuenta el número de elementos.

suma = 0
cantidad = 0
for num in nums:
    suma += num
    cantidad += 1
    
promedio = suma / cantidad
print(promedio)
