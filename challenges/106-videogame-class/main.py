# Desafio 106: Definir una clase que represente un videojuego con POO

class Videojuego:
    def __init__(self, titulo, genero, plataforma):
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.jugadores = 0

    def iniciar_juego(self):
        print(f"¡Iniciando {self.titulo} en {self.plataforma}!")

    def agregar_jugador(self):
        self.jugadores += 1
        print(f"Jugador agregado. Total de jugadores: {self.jugadores}")

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Género: {self.genero}, Plataforma: {self.plataforma}, Jugadores: {self.jugadores}")
        
# Ejemplo de uso
juego = Videojuego("Aventuras Épicas", "Aventura", "PC")
juego.iniciar_juego()
juego.agregar_jugador()
juego.mostrar_info()

# Explicación: La clase Videojuego tiene atributos como título, género y plataforma, y métodos para iniciar el juego, agregar jugadores y mostrar información del juego. 
# Esto demuestra los conceptos básicos de la programación orientada a objetos (POO) en Python.
