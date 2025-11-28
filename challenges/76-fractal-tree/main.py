# Desafío 76: Crear un programa que dibuje un fractal simple (árbol fractal) usando Turtle

# pip install turtle

import turtle
import random

def dibujar_arbol(t, tamaño, nivel):
    if nivel == 0:
        return
    t.forward(tamaño)
    angulo = random.randint(15, 45)
    t.left(angulo)
    dibujar_arbol(t, tamaño * 0.7, nivel - 1)
    t.right(2 * angulo)
    dibujar_arbol(t, tamaño * 0.7, nivel - 1)
    t.left(angulo)
    t.backward(tamaño)

pantalla = turtle.Screen()
pantalla.bgcolor("black")
t = turtle.Turtle()
t.color("white")
t.speed(0)
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
dibujar_arbol(t, 100, 5)
pantalla.exitonclick()
