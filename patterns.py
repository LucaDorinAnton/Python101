# Creating interesting patterns with Turtle Graphics and
# simple algorithms in Python3


import turtle
from turtle import *

import random

screen = turtle.Screen()
turtle.setup(850,850)
turtle.delay(0)
t = Turtle()


# Triangle
def trig():
    t.fd(100)
    t.left(120)
    t.fd(100)
    t.left(120)
    t.fd(100)
    t.left(120)

# Square
def square():
    for i in range(4):
        t.fd(100)
        t.left(90)

# Octogon
def oct():
    for i in range(8):
        t.fd(100)
        t.right(45)

# Parallelogram
def para():
    t.fd(100)
    t.left(60)
    t.fd(70)
    t.left(120)
    t.fd(100)
    t.left(60)
    t.fd(70)
    t.left(120)

# Combingin shapes

# 8 squares
def sq8():
    for i in range(8):
        square()
        t.left(45)

# 36 squares
def sq36():
    for i in range(36):
        square()
        t.right(10)

# coloring in

def colorsq():
    t.fillcolor("green")
    t.begin_fill()
    sq()
    t.end_fill()




def color_sq36():
    t.pencolor("blue")
    t.fillcolor("violet")
    for i in range(36):
        t.begin_fill()
        square()
        t.end_fill()
        t.right(10)

# adding randomness into the mix
def random_sq36():
    colors = ["red", "blue", "yellow", "green", "violet", "cyan"]
    t.penup()

    for i in range(36):
        t.fillcolor(random.choice(colors))
        t.begin_fill()
        square()
        t.end_fill()
        t.right(10)

# some fun with triangles
def tri_fun():
    colors = ["red", "blue", "yellow", "green", "violet", "cyan"]
    # colors = ["black", "white", "grey"]
    for i in range(6):
        t.fillcolor(random.choice(colors))
        t.begin_fill()
        trig()
        t.end_fill()
        t.right(60)

# more fun with more triangles
def meta_tri_fun():
    for i in range(6):
        tri_fun()
        t.fd(100)
        t.left(60)
        t.fd(100)


# Some advanced stuff (Fractals)

# Koch curve
def koch(depth):
    if depth == 0:
        t.fd(5)
    else:
        koch(depth-1)
        t.left(60)
        koch(depth-1)
        t.right(120)
        koch(depth-1)
        t.left(60)
        koch(depth-1)

def koch_flake(depth):
    t.penup()
    t.setpos(-200, -350)
    t.pendown()
    for i in range(6):
        koch(depth)
        t.left(60)

def sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        sierpinski(length/2,depth-1)
        t.fd(length/2)
        sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

def sierp(length, depth):
        t.penup()
        t.setpos(-200, -350)
        t.pendown()
        sierpinski(length, depth)

def draw():
    sierp(600, 7)

screen.onkeypress(draw, "space")
screen.listen()
turtle.done()
