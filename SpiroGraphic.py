import turtle
from turtle import *
import numpy as np
import random

my_turtle = turtle.Turtle()
my_turtle.speed(9999999999999999)
colors = ["red", "DeepPink3", "orange", "lime green", "cyan2", "DarkOrchid1", "bisque"]
a = 30.14159


def drawArt(d, angle, x, y):
    bgcolor(random.choice(colors))
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.pencolor(random.choice(colors))
    for i in range(1, 500):
        while my_turtle.pencolor() == bgcolor():
            my_turtle.pencolor(random.choice(colors))
        my_turtle.forward(d-14.5)
        my_turtle.left(angle)
        d -= 1
    turtle.clearscreen()


while a < 360:
    drawArt(15, a, 0, 0)
    a += 1
