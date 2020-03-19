import random
# Final Exam S'15
# Instructor: David Baldwin
# PROBLEM 1 - 10 Points
# PROBLEM 2 - 10 Points
# PROBLEM 3 - 10 Points
# PROBLEM 4 - 15 Points 
# PROBLEM 5 - 10 Points
# PROBLEM 6 - 15 Points
# PROBLEM 7 - 15 Points
# PROBLEM 8 - 15 Points
# TOTAL: 100 points
# PROBLEM 9 (bonus) - up to 30 Points

#     This exam is open book and open notes, but you may not access 
#     any Internet or networked sources.  You may not communicate with 
#     your classmates or outside parties aside from the instructor, 
#     electronically or otherwise. Any deviation from this policy 
#     will result in a grade of 0
#
#     Please 'write' your name below.  
#
# YOUR NAME GOES HERE
#
#     When you are finished, bring your laptop to the instructor for
#        submission details.


cs161autoruntests = False


# PROBLEM 1 - 10 Points
def canViewMovie(age, rating):
    '''Return True or False indicating whether a person of age can view a movie with rating.

    There are four ratings:
    G - general rating - suitable for all ages
    PG - you MUST be 8 years old or older
    PG-13 - you MUST be 13 years old or older
    R - you MUST be 17 years old or older
    Examples:
    >>> canViewMovie(17, 'G')
    True
    >>> canViewMovie(2, 'G')
    True
    >>> canViewMovie(12, 'PG')
    True
    >>> canViewMovie(12, 'PG-13')
    False
    >>> canViewMovie(6, 'PG')
    False
    >>> canViewMovie(3, 'R')
    False
    '''
    viewable = False
    if rating == "R" and age >=17:
        viewable = True
    elif rating == "PG-13" and age >=13:
        viewable = True
    elif rating == "PG" and age >=8:
        viewable = True
    elif rating == "G":
        viewable= True
    return viewable
    
# PROBLEM 2 - 10 points
def howManyBoxes(numItems, boxSize, availBoxes):
    '''Return the maximum number of full boxes (of size boxSize) you can use to pack numItems items.
    We allow only full boxes; the remaining items will not be packed.
    The maximum number of boxes returned must be less than the availBoxes.
    You must pack as many items as you can, given the availBoxes.

    Examples:
    >>> howManyBoxes(120, 25, 10)
    4
    >>> howManyBoxes(120, 25, 3)
    3
    >>> howManyBoxes(120, 5, 10)
    10
    '''
    finalBoxes=0
    finalBoxes= (numItems//boxSize)
    finalBoxes= min(finalBoxes , availBoxes)
    return finalBoxes


# PROBLEM 3 - 10 points
def countDigits(text):
    '''Return a count of the digits (0-9) that appear in text.

    Examples:
    >>> countDigits("Hi, I'm 12 years old.")
    2
    >>> countDigits('xxzz zzxx')
    0
    >>> countDigits('55 is the speed limit at 5PM')
    3
    >>> countDigits('123456 789')
    9
    >>> countDigits('1 ')
    1
    >>> countDigits('8x 9x 7x 6x!!')
    4
    '''
    digits = 0
    for i in text:
        if i in "0123456789":
            digits += 1
    return digits



# PROBLEM 4 - 15 points
def diceChecker(rolls):
    '''Return a list of 6 Boolean values indicating whether 1, 2, 3, 4, 5, 6 appears in rolls.

    rolls is a list of integers; each value in roles is 1, 2, 3, 4, 5, or 6
    The list that you return must have 6 Boolean values;
    element 0 indicates whether a 1 was ever rolled,
    element 1 indicates whether a 2 was ever rolled,
    etc.
    
    Examples:
    >>> diceChecker([1, 2, 3, 4, 5, 6, 6, 6, 1])
    [True, True, True, True, True, True]
    >>> diceChecker([6, 5, 4, 3, 1, 2])
    [True, True, True, True, True, True]
    >>> diceChecker([5, 5, 5])
    [False, False, False, False, True, False]
    '''
    check=[False,False,False,False,False,False]
    if 1 in rolls:
        check[0]=True
    if 2 in rolls:
        check[1]=True
    if 3 in rolls:
        check[2]=True
    if 4 in rolls:
        check[3]=True
    if 5 in rolls:
        check[4]=True
    if 6 in rolls:
        check[5]=True
    
    return check

# PROBLEM 5 - 10 points
def diceroller(n):
    '''Takes an integer `n` and returns a list of `n` random dice rolls
      (numbers between 1 and 6 inclusive). The `random` module has already 
      been imported for you.

      NOTE: The tests below are given for examples but passing them is
      not sufficient for full credit.  Full credit will be given for the
      correct call to the random module and correct code. Since we
      aren't using `seed`, you should expect to get different return
      contents from each call, but you should always get a list of
      length `n` in return

    >>> t = diceroller(2) 
    >>> t[0] >= 1 and t[0] < 7
    True
    >>> t[1] >= 1 and t[1] < 7
    True
    >>> t = diceroller(10)
    >>> t[9] >= 1 and t[9] < 7
    True
    >>> t = diceroller(100)
    >>> t[99] >= 1 and t[99] < 7
    True
    >>> all([x>=1 and x<7 for x in t]) # check all values are between 1 and 6
    True

    '''
    callList=[]
    for i in range(n):
        callList.append(random.randrange(1,7))
    return callList




# PROBLEM 6 - 15 points
# Translate the code in `everyOtherFor` to use a `while` loop instead of a `for` loopo
# and place the result inside `everyOtherWhile`
def everyOtherFor(numList):
    '''Return a new list of numbers consisting of the 1st, 3rd, 5th, etc.... elements of numList.

    numList must not be mutated.
    Examples:
    >>> inList = [-5, 0, 5, 20, -123]
    >>> everyOtherFor(inList)
    [0, 20]
    >>> inList
    [-5, 0, 5, 20, -123]
    >>> everyOtherFor([1, 3, 4, 5, 0, 10])
    [3, 5, 10]
    '''
    res = []
    for i in range(1,len(numList),2):
        res.append(numList[i])
    return res


def everyOtherWhile(numList):
    '''Return a new list of numbers consisting of the 1st, 3rd, 5th, etc.... elements of numList using
    only a while loop (no `for` or slice notation allowed)
    
    numList must not be mutated.

    Examples:

    >>> inList = [-5, 0, 5, 20, -123]
    >>> everyOtherWhile(inList)
    [0, 20]
    >>> inList
    [-5, 0, 5, 20, -123]
    >>> everyOtherWhile([1, 3, 4, 5, 0, 10])
    [3, 5, 10]

    '''
    res = []
    n=0
    while n<len(numList):
        if not n%2==0:
            res.append(numList[n])
        n+=1 
    return res


# PROBLEM 7 - 15 points
# create_zeroed_image  and print_image from Ex.5 sre provided, you are to write
#   create_star_image
def create_zeroed_image(n):
    """create_zeroed_image takes an integer `n` and returns an n-by-n
    list of lists containing all zeros
    """
    retlist = []
    for i in range(n):
        innerlist = []
        for j in range(n):
            innerlist.append(0)
        retlist.append(innerlist)

    return retlist

def print_image(img):
    """print_image pretty-prints a matrix image"""
    for k in img:
        print("".join([str(x) for x in k] ))


def create_star_image(n):
    """create_star_image takes an odd integer `n` and returns an n-by-n
    list of lists containing the image of a star.  A star is defined as follows
    
    1) Both diagonals are filled with ones (HINT: This is the same as the 'X image' in Ex.5)
    2) The (n//2)th column is filled with ones
    3) The (n//2)th row is filled with ones

    If n is negative or zero, raise an Exception

Output of print_image(create_star_image(5))
10101
01110
11111
01110
10101

Output of print_image(create_star_image(7))
1001001
0101010
0011100
1111111
0011100
0101010
1001001

>>> create_star_image(-1)
Traceback (most recent call last):
    File "/usr/lib/python3.4/doctest.py", line 1324, in __run
       compileflags, 1), test.globs)
    File "<doctest __main__.create_star_image[0]>", line 1, in <module>
       create_star_image(-1)
    File "finalsol.py", line 260, in create_star_image
       raise Exception("n must be > 0")
Exception: n must be > 0

>>> create_star_image(7)
[[1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1]]
>>> create_star_image(5)
[[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]
>>> create_star_image(1)
[[1]]
>>> create_star_image(3)
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
>>> create_star_image(11)
[[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
    """
    img=create_zeroed_image(n)
    if n <= 0:
        raise Exception("n must be > 0")
    for i in range (n):
        for j in range (n):
            img[i][i]=1
            img[i][n-i-1]=1
            img[i][n//2]=1
            img[n//2][j]=1
            
    return img

# PROBLEM 8 - 15 points
#
# Design a class that represents a light switch called Lightswitch.
#   Your light switch class should have a constructor that accepts the
#   initial state of the switch (on/off) and two methods
#
#   toggle_switch()
#       Takes no arguments and returns nothing, toggles the light switch on and off
#
#   is_light_on()
#       Takes no arguments and returns a boolean indicating whether or not the light is switched on
class LightSwitch:
    """

    A class that represents a light switch 

    >>> li = LightSwitch(False)
    >>> li.is_light_on()
    False
    >>> li.toggle_switch()
    >>> li.is_light_on()
    True
    >>> li.toggle_switch()
    >>> li.is_light_on()
    False
    >>> li.is_light_on()
    False

    """
    def __init__(self, lightState):
        self.lightState = lightState
        

    def toggle_switch(self):
        if self.lightState == True:
            self.lightState= False
        if self.lightState == False:
            self.lightState= True
    def is_light_on(self):
        if self.lightState:
            return True
        return False
            
        


# PROBLEM 9 (BONUS)
def lightswitch_game(n):

    """Consider the following game. There are `n` light switches numbered sequentially from 0 to `n-1`. All of the lights are initially off.
    
    We go through a series of `n` steps.

    On the first step, we toggle all the lights
    On the second step, we toggle every other light starting from the 0th (0,2,4,etc.)
    On the third step, we toggle every third light starting from the 0th (0,3,6,etc.)
    On the fourth step, we toggle every fourth light starting from the 0th (0,4,8,etc.)
    ...
    On the nth step, we toggle every nth light starting from the 0th (0,n,2n,3n,etc.)


    lightswitch_game returns a list of all the of lights that are
    still on.  Use your LightSwitch class to keep track of a single
    light switch.

    Note: Generating the correct answer is not sufficient, you *MUST*
    simulate this process to get credit. In other words, even if you
    find a pattern in the answer (there is one, this is a well known
    math problem), you only get credit if you simulate flipping of the 
    light switches

>>> lightswitch_game(100) 
[0, 3, 8, 15, 24, 35, 48, 63, 80, 99]

    """
    switchList=[]
    for i in range(n):
        switchList.append(False)
    switchList = LightSwitch(switchList)
    for i in range(n):
        switchList[i].toggle_switch()
    for i in range(0,n,2):
        switchList[i].toggle_switch()
    for i in range (0,n,3):
        switchList[i].toggle_switch()
        
    return switchList


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
