import math
#################################################################
#   CS161 S15  -  Instructor: David Baldwin (dbaldwin@pdx.edu)
#   Programming Exercise #4
#   Due 5/1
#
#
#
#   CONTENTS:
#    SECTION I
#       a),b),c)
#
#   
#   SUBMISSION INSTRUCTIONS:
#
#   Submit ths file to D2L
#
#   MINIMUM PASSING REQUIREMENTS: 
#   A fully correct solution (one that
#   passes all the tests) to at least one of the problems


################################################################
#  OPTIONS
#
#  Set this value to True if you want the IDLE to run
#      all the tests every time you run this file
cs161autoruntests = False

# SECTION I

# Part a)
def count_num_chars(astr,achar):
    """ count_num_chars takes in a string astr and a single character string
    achar (see examples) and returns an integer indicating how many times
    achar is in the string

>>> count_num_chars("","a")
0
>>> count_num_chars("abcd","a")
1
>>> count_num_chars("bb","b")
2
>>> count_num_chars("ababa","b")
2
>>> count_num_chars("ababa","a")
3
>>> count_num_chars("ababa","z")
0
>>> count_num_chars("abcdabcdabcdabcd","d")
4
>>> count_num_chars("abcdabcdabcdabcd","a")
4
>>> count_num_chars("aaaaaaaa","a")
8
    """
    return None

# Part b)
def count_consonants(astr):
    """ count_non_vowels takes in a string and returns an integer
    indicating how many consonants are in the string.  Don't worry about
    numbers or symbols (#)

>>> count_consonants("aaaaaaaa")
0
>>> count_consonants("bbbbbbbb")
8
>>> count_consonants("")
0
>>> count_consonants("aeiou")
0
>>> count_consonants("qwerty")
5
>>> count_consonants("zzt")
3
    """
    return None

# Part c)
def sum_upto_divisible(start,stop,div):
    """sum_upto_divisible takes an integer start, an integer stop and an
    integer div and returns an integer representing the sum of all
    digits from start to stop-1 that are divisible by div.
    
    This is the same function as exercise 3, but now you must implement
    it with `for`. Do NOT use `while`


NOTE: 1+2 = 3
>>> sum_upto_divisible(0,3,1)
3

NOTE: 5+10+15+20 = 50
>>> sum_upto_divisible(0,25,5)
50
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
