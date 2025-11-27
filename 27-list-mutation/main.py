# Desafío 27: Que imprime esto?
a = [1, 2]
b = a
a += [3]
print(a, b)
# Resultado: [1,2,3] [1,2,3]
# Explicación: Como las listas son mutables, cuando hacemos a += [3], modificamos la lista original
# que ambas variables comparten, por eso ambas muestran [1,2,3]
