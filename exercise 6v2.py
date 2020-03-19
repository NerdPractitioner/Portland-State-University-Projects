import math
################################################################
#   CS161 S15  -  Instructor: David Baldwin (dbaldwin@pdx.edu)
#   Programming Exercise #6
#   Due: 5/29
# 
#   In this exercise, we will introduce objects to write a cleaner and more 
#     maintainable implementation of the soda machine seen in homework 1
# 
#   NOTE: to run individual tests on class methods, use 
# 
# >>> runtest(ClassName.methodname)
#
#   For example 
#
# >>> runtest(SodaMachine.validsoda)
#
#   CONTENTS:
#   Section I 
#      a
#   Section II
#      a,b (no tests!)
#
#   SUBMISSION INSTRUCTIONS:
#
#   Submit ths file to D2L
#
#   MINIMUM PASSING REQUIREMENTS: 
#   A correct class definition in Section I and at least one correct
#      solution for Section II
#
# Below is the code from Homework 1 for your reference
#
# def initsodas():
#    """ Returns a "sodasupply" to be passed to other functions"""
#    sodasupply = { "Lemon": 3, "Cola": 2, "Root Beer": 4 , "Diet": 0 }
#    return sodasupply
#
# def validsoda(sodasupply,sodaname):
#    """ Takes a "sodasupply" and a string sodaname and returns a boolean
#           indicating whether the string is a valid soda name
#    """
#    return  (sodaname in sodasupply)
#
#def countsoda(sodasupply,sodaname):
#    """ Takes a "sodasupply" and a string sodaname and returns a integer
#           representing the number of sodas of type sodaname in the machine
#    """
#     
#    if not validsoda(sodasupply,sodaname):
#        raise ValueException("Invalid soda!")
#    return sodasupply[sodaname]
#
# def retrievesoda(sodasupply,sodaname):
#    """ Takes a "sodasupply" and a string sodaname and returns a string
#           indicating a soda of type sodaname has been removed from the machine
#           This updates the "sodasupply" with the new number of sodas
#
#           Right now, our 'soda' is just a string "<sodaname> placeholder"
#           Mmm. Delicious!
#    """
#    if not validsoda(sodasupply,sodaname):
#        raise Exception("Invalid soda!")
#
#    if not countsoda(sodasupply,sodaname)>0:
#        raise Exception("No sodas of this type are left")
#
#    sodasupply[sodaname]-=1;
#    return "%s placeholder" % sodaname
#
# def printsodas(sodasupply):
#    """ Takes a "sodasupply" and returns None
#           This function will print type of soda and number of each 
#    """
#    for k in sodasupply:
#        print("%s: %d left" % (k,sodasupply[k]))


################################################################
#  OPTIONS
#
#  Set this value to True if you want the IDLE to run
#      all the tests every time you run this file
cs161autoruntests = True


# SECTION I
# Part a)
#   Create a class Soda that contains member variables `name` and `price`.  Include 
#     an appropriate constructor
class Soda:
    """

>>> s = Soda("Cola",100)
>>> s.name == "Cola"
True
>>> s.price == 100
True

    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
        return

# SECTION II
# Part a) and b) are inside the class definition
class SodaMachine:
    """
    The class SodaMachine represents the operations of a soda machine


    """
    def __init__(self, adict):
        """ SodaMachine's contructor that takes a dictionary mapping strings
            to integers `adict`.  The constructor sets the the 
            member variable `sodasupply` to `adict`

>>> k = SodaMachine({"Cola":1})
>>> b = SodaMachine({"Cola":1,"Pizza":2})
>>> k.sodasupply = {"Cola":1}
>>> b.sodasupply = {"Cola":1,"Pizza":2}
        """
        self.sodasupply = adict
        

    def validsoda(self,sodaname):
        """ Takes a string sodaname and returns a boolean indicating whether the string is a valid soda name
         for this object's sodasupply

>>> k = SodaMachine({"Cola":1})
>>> b = SodaMachine({"Cola":1,"Pizza":2})
>>> k.validsoda("Cola")
True
>>> k.validsoda("PIzza")
False
>>> k.validsoda("Pizza")
False
>>> b.validsoda("Pizza")
True
>>> b.validsoda("Grape")
False
        """
        return  (sodaname in self.sodasupply)


    def countsoda(self,sodaname):
        """ Takes  string sodaname and returns a integer
        representing the number of sodas of type sodaname in the machine

>>> b = SodaMachine({"Cola":1,"Pizza":2})
>>> k = SodaMachine({"Cola":1})
>>> k.countsoda("Cola")
1
>>> b.countsoda("Pizza")
2
>>> b.countsoda("Cola")
1
        """
     
        if not self.validsoda(sodaname):
            raise Exception("Invalid soda!")
        return self.sodasupply[sodaname]

    # Part a)
    # Implement the retrievesoda function.  Instead of returning a 
    #    string "Soda placeholder", return a new instance of your Soda
    #    object with the `sodaname` as the name and a price of 100
    def retrievesoda(self,sodaname):
        """ Takes a string sodaname and returns a string
           indicating a soda of type sodaname has been removed from the machine
          This updates the "sodasupply" with the new number of sodas

           Return a soda object with `sodaname` as the name and a price of 100
           Mmm. Delicious!

>>> b = SodaMachine({"Cola":1,"Pizza":2})
>>> s1 = b.retrievesoda("Pizza")
>>> s1.name == "Pizza"
True
>>> s1.price == 100
True
>>> s2 = b.retrievesoda("Pizza")
>>> s2.name == "Pizza"
True
>>> b.retrievesoda("Pizza")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "exercise6.py", line 143, in retrievesoda
    raise Exception("No sodas of this type are left")
Exception: No sodas of this type are left
>>> s3 = b.retrievesoda("Cola")
>>> s3.name == "Cola"
True
>>> b.sodasupply["Pizza"] == 0 and b.sodasupply["Cola"] == 0
True

        """
    def retrievesoda(sodasupply,sodaname):
        if not validsoda(self.sodasupply,sodaname):
            raise Exception("Invalid soda!")

        if not countsoda(self.sodasupply,sodaname)>0:
            raise Exception("No sodas of this type are left")

        self.sodasupply[sodaname]-=1;
        return "%s placeholder" % sodaname
        return None

    # Part b)
    def printsodas(sodasupply):
        for k in sodasupply:
            print("%s: %d left" % (k,self.sodasupply[k]))
    # Implement the printsodas function 




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
