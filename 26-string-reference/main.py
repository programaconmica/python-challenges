# Desafío 26: Que imprime esto?

x = y = 'Py'
x += 'thon'
print(x, y)

# Resultado: Python Py
# Explicacion: x = y = 'Py' hace que tanto x como y apunten inicialmente al mismo objeto string 'Py'.
# x += 'thon' no modifica el string original, porque los strings en Python son inmutables. 
# Lo que ocurre realmente es: x = x + 'thon'.
# y sigue apuntado a 'Py' y x apunta a un nuevo objeto 'Python'
