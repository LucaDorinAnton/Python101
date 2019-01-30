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

# Increment the number in the signature with respect to
# the person who's working above you!
#
# For example, if the person above you is working on:
#  ---
#  def draw5():
#  ---
#  You should be working on "def draw6()" !!!

# Make sure to write your name in a comment before the function you designed,
# in order to be able to attribute it to you in the end!
# Example:
# ---
# author= John Doe Smith
# def draw10():
    # Doing cool things with my turtle

# Each function will be called sequentially. Your turtle will always
# start from the center, with black outline and fill color, blank screen
# and pointing right!

# If you want to test your drawing,
# Go to https://trinket.io/features/pygame
# Clear the main.py template you get
# and paste all the code from the file
# challenge-test-my-code.py over the main.py file


# You are free to import modules!

# You are free to write additional helper functions!
# (As long as your draw function is the last one in your code...)

# You are free to look at other peoples code for inspiration.
# If there are very similar designs though, first one to run will count
# so don't just try to copy the most complicated design!
# That won't work!

# DO NOT MESS WITH ANY CODE EXCEPT YOUR OWN!
# ZERO_TOLERANCE POLICY - If I catch you doing that, I'll kick you
# from the competition and disqualify you from the contest

# If you're code crashes in any way, you are disqualified!

# If your code takes longer than 30 seconds, you will be disqualified!

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
# t.circle(r) -> draw a circle with radius r

import turtle
from turtle import *

import random
import signal
import time

screen = turtle.Screen()
turtle.setup(850,850)
t = Turtle()

# List of colors which you can use
cols = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
# You can also use hexidecimal colors if you want more precision.
# t.fillcolor("#FF00FF")

# You can find a color wheel here
# (in order to choose hexadecimal values):
# https://www.w3schools.com/colors/colors_picker.asp


# Helper functions (feel free to use this in your code!)

def trig(side_len, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.fd(side_len)
        t.left(120)
    t.end_fill()

def sq(side_len, color):
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
    sq(100, "red")

def draw2():
    oct(100, "green")

def draw3():
    trig(50, "blue")
    asfdjhasdljfkhasdj



# --------------------------------------
# DO NOT EDIT ANY CODE BELOW THIS LINE!
# --------------------------------------

funcs = [draw1, draw2, draw3]

def cleanup():
    screen.clearscreen()
    screen.onkeypress(press, "space")
    screen.onkeypress(cleanup, "a")
    turtle.delay(0)
    global t
    t = Turtle()

def run_func():
    signal.alarm(30)
    try:
        funcs[cnt]()
    except Exception as timeout:
        print("WARNING !!!")
        if timeout.args[0] == "end of time":
            print("Drawing number " + str(cnt + 1) + " timed out!")
            print("Drawing number " + str(cnt + 1) + " is disqualified!")
        else:
            print("Drawing number " + str(cnt + 1) + " raised an exception!")
            print("Drawing number " + str(cnt + 1) + " is disqualified!")
    signal.alarm(0)
    return None

def handler(signum, frame):
    print("Drawing number " + str(cnt + 1) + " timed out!")
    print("Drawing number " + str(cnt + 1) + " is disqualified!")
    raise Exception("end of time")

cnt = 0
def press():
    global cnt
    if cnt < len(funcs):
        cleanup()
        print("Running drawing number: " + str(cnt + 1))
        run_func()
        cnt += 1
    else:
        print("Done!")

signal.signal(signal.SIGALRM, handler)
cleanup()
screen.listen()
turtle.done()
