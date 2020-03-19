Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
from turtle import *

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
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/matthewholmes/Documents/turtle 1.py", line 1, in <module>
    from turtle import *
  File "/Users/matthewholmes/Documents/turtle.py", line 1
    Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03)
             ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
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
