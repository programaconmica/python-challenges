# Desafío 34: Comprobá si dos palabras son anagramas
a = "roma"
b = "amor"
# Ordenamos ambas palabras con sorted().
# Si las listas ordenadas de letras coinciden, son anagramas.
print(sorted(a) == sorted(b))
