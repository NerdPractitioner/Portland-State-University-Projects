import math
#################################################################
#   CS161 S15  -  Instructor: David Baldwin (dbaldwin@pdx.edu)
#   Programming Exercise #5
#   Due: 5/15
# 
#   In this exercise, we will experiment with manipulating nested data
#   structures.  In computer graphics, images are often represented by
#   n-by-n matricies - in Python, this is like having a list of n
#   lists, each containing n elements each.  Each element represents
#   the color of a pixel.  
# 
#   In our exercise, we will be working with black and white 'images'
#   0 will represent black and 1 will represent white.  The function 
#   `print_image` is provided and "pretty prints" the list of lists in 
#   a more  visually appealing format
#  
#   For example 
#
#   >>> img = [[1,0],[0,1]]
#   >>> print_image(img)
#   10
#   01
#  
#   In the following five problems, you will attempt to programmatically
#   make these lists with certain properties.
#
#   CONTENTS:
#    SECTION I
#       a),b),c), d)
#    SECTION II 
#       a)  
#   
#   SUBMISSION INSTRUCTIONS:
#
#   Submit ths file to D2L
#
#   MINIMUM PASSING REQUIREMENTS: 
#
#   A fully correct solution (one that
#   passes all the tests) to at least two of the problems


################################################################
#  OPTIONS
#
#  Set this value to True if you want the IDLE to run
#      all the tests every time you run this file
cs161autoruntests = False

# You may find this function useful when debugging
def print_image(img):
    """print_image pretty-prints a matrix image"""
    for k in img:
        print("".join([str(x) for x in k] ))


# Part a)
def create_zeroed_image(n):
    """create_zeroed_image takes an integer `n` and returns an n-by-n
    list of lists containing all zeros

Output of print_image(create_zeroed_image(5))
00000
00000
00000
00000
00000

>>> create_zeroed_image(5)
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> create_zeroed_image(0)
[]
>>> create_zeroed_image(1)
[[0]]
>>> create_zeroed_image(2)
[[0, 0], [0, 0]]
>>> create_zeroed_image(4)
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """

    alist = []
    for i in range(0, n):
        alist.append([])
        for j in range(0,n):
            alist[i].append(0)
    return alist

# Part b)
def create_diagonal_image(n):
    """create_zeroed_image takes an integer `n` and returns an n-by-n
    list of lists containing all zeros execpt for the diagonal
    starting from the upper left corner going to the lower right
    corner, which shall be all 1s

    HINT: reuse your create_zeroed_image and change the output

Output of print_image(create_diagonal_image(5))
10000
01000
00100
00010
00001


>>> create_diagonal_image(5)
[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
>>> create_diagonal_image(2)
[[1, 0], [0, 1]]
>>> create_diagonal_image(1)
[[1]]
>>> create_diagonal_image(10)
[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    """
    alist = []
    for i in range(0, n):
        alist.append([])
        for j in range(0,n):
            if i ==j:
                alist[i].append(1)
            else:
                alist[i].append(0)

    ##########
 #   img = create_zeroed_image(n)
   # for i in range(n):
#        for j in range(n):
#            if i == j:
#                img[i][j] = 1
    #######
    
    return alist

# Part d)
def create_x_image(n):
    """create_x_image takes an integer `n` and returns an n-by-n
    list of lists containing the image of an "X"

Output of print_image(create_x_image(5))
10001
01010
00100
01010
10001

>>> create_x_image(5)
[[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
>>> create_x_image(4)
[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
>>> create_x_image(1)
[[1]]
>>> create_x_image(2)
[[1, 1], [1, 1]]
>>> create_x_image(3)
[[1, 0, 1], [0, 1, 0], [1, 0, 1]]
>>> create_x_image(10)
[[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    """
    alist = create_diagonal_image(n)
    for i in range(0, n):
        alist[i][i]=1
        alist[i][n-1-i]=1
    return alist

# part e)
def create_border_image(n):
    """create_border_image takes an integer `n` and returns an n-by-n
    list of lists containing all zeros execpt for the border 
    of the image

Output of print_image(create_border_image(5)):
11111
10001
10001
10001
11111

>>> create_border_image(5)
[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
>>> create_border_image(5)
[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
>>> create_border_image(2)
[[1, 1], [1, 1]]
>>> create_border_image(1)
[[1]]
>>> create_border_image(4)
[[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    """
    img=create_zeroed_image(n)
    for i in range(n):
        for j in range(n):
            img[i][0]=1
            img[0][j]=1
            img[i][n-1]=1
            img[n-1][j]=1
    return img

#Section II
# Part a)
# Your task is to complete to code below
def read_image(filename):
    """ read_image takes a string filename and reads in a 
        file. From this file, it creates a new matrix based 
        on the contents. Several example files are available
        in the homework directory.

        Documentation for the enumerate function can be found at 

    https://docs.python.org/3/library/functions.html#enumerate


>>> read_image("testinput1.txt")
[[0, 1, 0], [1, 0, 1], [0, 1, 0]]
>>> read_image("testinput2.txt")
[[1]]
>>> read_image("testinput3.txt")
[[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]


"""
    try:
        fi = open(filename,"r")
        lines = fi.readlines()
        n = int(lines[0]);
        img = create_zeroed_image(n)
        for i,line in enumerate(lines[1:]):
            clean_line = line.strip() # remove whitespace and newlines
            for j,char in enumerate(clean_line):
                # your code here
    
                img[i][j]=char
                # end your code here
        return img
    except IOError:
        raise Exception("Cannot find file " + filename);
    finally:
        fi.close()
    
# END OF ASSIGNMENT

#### LIBRARY FUNCTIONS
# DO NOT MODIFY


import sys
import doctest
import builtins

cs161print = True
cs161veryverbose = False
if cs161print:
    def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        tup = objects
        if len(objects) and cs161veryverbose:
            lo = list(objects)
            lo = ["***PRINT OUTPUT***"]+lo +["\n***END PRINT OUTPUT***"]
            lo[1] = "\n"+str(lo[1])
            tup = tuple(lo)
        else:
            tup = objects
        builtins.print(*tup,sep=sep,end=end,file=sys.stderr,flush=flush)


def runalltests():
    """ Run all tests in this assignment """
    doctest.testmod()
    
def runtest(testname,verbose=False):
    if type(testname) is type(runtest):
        doctest.run_docstring_examples(testname,None,verbose)
        builtins.print("\n");
    else:
        builtins.print( "Your input is not a function!")


if cs161autoruntests and __name__ == "__main__":
    runalltests()
