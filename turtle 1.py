from turtle import *

# Turtle docs:   https://docs.python.org/3.4/library/turtle.html
def square(size, color):
    pendown()
    fillcolor(color)
    begin_fill()
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    begin_fill
    forward(size)
    left(90)
    end_fill()
    penup()
    
# Part A) Run this in the interpreter
square(100, "red")


# Part B) Draw two non-overlapping squares
right(90)
square(100, "blue")
forward(100)
square(100, "green")

# Part C) Draw two non-overlapping squares, filled with different colors, (see the doucmentation for fill_color, begin_fill, end_fill
