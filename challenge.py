# Let's have some fun!
#  Everyone log in to https://www.repl.it with the link:
# ---
#
# ---
#
# and copy the method signature below!

# author = Luca-Dorin Anton
# def draw1():
    # do something interesting!

# increment one to the number in the signature from
# the person who's working above you!
#
# For example, if the person above you is working on:
#  ---
#  def draw5():
#  ---
#  You should be working on "def draw6()" !!!

# Make sure to write your name ina comment before the function you designed,
# in order to be able to attribute it to you in the end!
# Example:
# ---
# author= John Doe Smith
# def draw10():
    # Doing cool things with my turtle

# Each function will be called sequentially. Your turtle will always
# start from the center, with black outline and fill color, blank screen
# and pointing right!

# You are free to import modules
# and look at other peoples code for inspiration
# If there are very similar designs though, first one to run will count
# only, so don't just try to copy the most complicated design! That
# won't work!

# If you're code crashes in any way, you are disqualified

# Screen size will be set to 850x850 pixels! You start in the middle.
# Take that into account!

# Coolest design wins the challenge! Good luck and happy coding!

# ------------------
# FUNCTION REFERENCE
# ------------------

# t.fd(x) -> move forward x pixels
# t.bk(x) -> move backwards x pixles
# t.right(x) -> turn right x degrees
# t.left(x) -> turn left x degrees
# t.penup() -> stop drawing
# t.pendown() -> start drawing again
# t.pencolor(col) -> set the color of the pen to col
# t.fillcolor(col) -> set the color used to fill in shapes to col
# t.begin_fill() -> start filling in a shape (call before starting a simple shape)
# t.end_fill() -> complete the shape fill (call just after finishing a simple shape)


import turtle
from turtle import *

import random

screen = turtle.Screen()
turtle.setup(850,850)
turtle.delay(0)
t = Turtle()

# List of colors which you can use
cols = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
# You can also use hexidecimal colors if you want more precision.
# t.fillcolor("#FF00FF")


# Helper functions (feel free to use this in your code!)

def trig(side_len, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.fd(side_len)
        t.left(120)
    t.end_fill()

def square(side_len, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(side_len)
        t.left(90)
    t.end_fill()

def oct(side_len,color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(8):
        t.fd(side_len)
        t.left(45)
    t.end_fill()

def para(side_len1,side_len2, color, angle):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(side_len1)
    t.left(angle)
    t.fd(side_len2)
    t.left(180 - angle)
    t.fd(side_len1)
    t.left(angle)
    t.fd(side_len2)
    t.left(180 - angle)
    t.end_fill()


def draw1():
