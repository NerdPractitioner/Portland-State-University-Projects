
#################################################################
#   CS161 S15  -  Instructor: David Baldwin (dbaldwin@pdx.edu)
#   Practice Midterm


cs161autoruntests = False
# DO NOT MODIFY
def is_special(x):
    """ is_special takes an integer x and returns a boolean
    indicating if this is a 'special' number"""
    return ((3)&x)==3
# END DO NOT MODIFY

# PROBLEM 1
def both_special(a,b):
    """ both_special takes an integer `a` and an integer `b`
        and returns true iff both integers are `special` 

>>> both_special(0,3)
False
>>> both_special(3,0)
False
>>> both_special(3,3)
True

>>> both_special(100,1)
False
>>> both_special(100,191)
False
>>> both_special(9,109)
False
>>> both_special(267,11)
True
>>> both_special(3,11)
True
    """
    if is_special(a) and is_special(b):
         return True
    return False

# PROBLEM 2
# Implement using both a while and for loop
def sum_special(start,stop):
    """ sum_special takes an integer `start` and an integer `stop`
        and returns the sum of all special numbers between `start`
        and `stop`

>>> sum_special(0,3)
0
>>> sum_special(3,4)
3
>>> sum_special(4,4)
0
>>> sum_special(0,10)
10
>>> sum_special(5,10)
7
>>> sum_special(50,100)
975
>>> sum_special(100,1000)
123975
>>> sum_special(10000,1000)
0



    """
    marker = start
    suma = 0
    while marker < stop:
         if is_special(marker):
              suma += marker
         marker +=1
    return suma
# PROBLEM 3
def largest_special(start,stop):
    """ largest_special takes an integer `start` and an integer `stop`
        and returns the *largest* integer between `start` and `stop` 
        that is special


        If there are no special numbers between `start` and `stop` 
        return 0

>>> is_special(3)
True
>>> is_special(4)
False
>>> largest_special(0,5)
3

>>> largest_special(0,25)
23
>>> largest_special(0,100)
99
>>> largest_special(25,100)
99
>>> largest_special(100,109)
107
>>> largest_special(100,175)
171
    """
    specL = 0
    for i in range(start+1, stop):
         if is_special(i):
              specL = max(specL, i)   
    return specL

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
