# Desafio 88: Generar 1000 mails con tu nombre

nombre = input("Ingresa tu nombre: ")
cantidad = 1000

for i in range(cantidad):
    mail = f"{nombre}{i}@mail.com"
    print(mail)
    
# Explicación: El programa pide un nombre y genera 1000 correos electrónicos numerados secuencialmente.
