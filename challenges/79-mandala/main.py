# Desafío 79: Crear un programa que dibuje un mandala con Turtle

# pip install turtle

import turtle
import random

def dibujar_mandala(t, tamaño, repeticiones):
    for _ in range(repeticiones):
        t.circle(tamaño)
        t.right(360 / repeticiones)
        t.color(random.random(), random.random(), random.random())

pantalla = turtle.Screen()
pantalla.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
dibujar_mandala(t, 100, 36)
pantalla.exitonclick()