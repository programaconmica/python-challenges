# Desafío 25: Mostrar solo las claves de un diccionario

persona = {"nombre": "Luis", "edad": 28}
print(list(persona.keys()))

for clave in persona.keys():
    print(clave)
    
# Explicación: keys() devuelve una vista de las claves, que convertimos a lista.
