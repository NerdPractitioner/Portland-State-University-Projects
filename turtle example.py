Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> from turtle import *

# Turtle docs:   https://docs.python.org/3.4/library/turtle.html
def square(size):
    pendown()
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    penup()
    
# Part A) Run this in the interpreter
square(100)

# Part B) Draw two non-overlapping squares

# Part C) Draw two non-overlapping squares, filled with different colors, (see the doucmentation for fill_color, begin_fill, end_fill

SyntaxError: multiple statements found while compiling a single statement
>>> 
