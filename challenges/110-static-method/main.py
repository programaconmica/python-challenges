# Desafio 110: Hacer una clase con un metodo estatico

class Calculadora:
    @staticmethod
    def sumar(a, b):
        """Suma dos números sin necesidad de instancia"""
        return a + b
    
    @staticmethod
    def restar(a, b):
        """Resta dos números sin necesidad de instancia"""
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        """Multiplica dos números sin necesidad de instancia"""
        return a * b
    
    @staticmethod
    def dividir(a, b):
        """Divide dos números sin necesidad de instancia"""
        if b == 0:
            return "No se puede dividir por cero"
        return a / b

# Ejemplo de uso sin instanciar la clase
print("Suma:", Calculadora.sumar(10, 5))
print("Resta:", Calculadora.restar(10, 5))
print("Multiplicación:", Calculadora.multiplicar(10, 5))
print("División:", Calculadora.dividir(10, 5))

# Explicación: Los métodos estáticos se definen con el decorador @staticmethod 
# y no requieren de una instancia de la clase (self) para ser utilizados. 
# Se llaman directamente desde la clase usando el nombre de la clase seguido 
# del método (Clase.metodo()).
