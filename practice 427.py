def filter_evens(nums):
  """ filter_evens takes a list of integers and returns a new
        list of integers including only the odd numbers

>>> filter_evens([])
[]
>>> filter_evens([2,4,6])
[]
>>> filter_evens([1,3,5])
[1, 3, 5]
>>> filter_evens([1,2,3,4,5,6])
[1, 3, 5]
>>> filter_evens(list(range(10)))
[1, 3, 5, 7, 9]
  """


def filter_vowels(astr):
  """ filter_vowels takes a string and returns a string
        without vowels

>>> filter_vowels("aeiou")
''
>>> filter_vowels("hello")
'hll'
>>> filter_vowels("omglolbbq")
'mgllbbq'
>>> filter_vowels("bcdfg")
'bcdfg'
    """

    retstr = ""
    for char in astr:
        # if not (char in "aeiou")
        if not char == "a" or char=="e" or char=="i" or char=="o" or char=="u":
            retstr += char
    5return retstr

def filter_vowel_list(strs):
  """ filter_vowels takes a list of strings and returns a list of strings
        without vowels
>>> filter_vowel_list(["aeiou"])
['']
>>> filter_vowel_list(["aeiou","hello","omglolbbq"])
['', 'hll', 'mgllbbq']

NOTE: list(str) produces a list of single characters in str

>>> filter_vowel_list( list("abcdefghijklmnopqrstuvwxz"))
['', 'b', 'c', 'd', '', 'f', 'g', 'h', '', 'j', 'k', 'l', 'm', 'n', '', 'p', 'q', 'r', 's', 't', '', 'v', 'w', 'x', 'z']

    """
    retstr = []
    for astr in strs:
        retstr.append (filter_vowels(astrs))
    return retstr

def filter_vowel_list(strs):
  """ filter_vowels takes a list of strings and returns a list of strings
        without vowels
>>> filter_vowel_list(["aeiou"])
['']
>>> filter_vowel_list(["aeiou","hello","omglolbbq"])
['', 'hll', 'mgllbbq']

NOTE: list(str) produces a list of single characters in str

>>> filter_vowel_list( list("abcdefghijklmnopqrstuvwxz"))
['', 'b', 'c', 'd', '', 'f', 'g', 'h', '', 'j', 'k', 'l', 'm', 'n', '', 'p', 'q', 'r', 's', 't', '', 'v', 'w', 'x', 'z']

    """

def max_int_list(nums_list):
  """ max_int_list takes a list of list of integers and returns the 
        largest one

>>> max_int_list([[1,2,3,4]])
4
>>> max_int_list([[1,2,3,4],[1,2,3,5]])
5
>>> max_int_list([[1,2,3,4],[10],[1,2,3,5]])
10
>>> max_int_list([[1,2,3,4],[10],[1,2,3,5],[1000]])
1000
    """
    for num in nums_list
        max (num)
    return num

def swap_list_elements(num_list,i,j):
  """swap_list_elements of list of integers and two index integers 
        i and j 

     The function returns None and swaps the elements at index i and j
     in num_list

  """


def sum_diag(nums_list):
  """sum_diag takes a list of list of integers.  You may
        assume that all lists are of the same length and the number
        of lists is the same as the length of each list.
    
     In other words, `nums_list` is a 2D, k by k list

  The function computes the sum of the diagonal 
  """





def transpose_int_list(nums_list):
  """transpose_int_list takes a list of list of integers.  You may
        assume that all lists are of the same length and the number
        of lists is the same as the length of each list.
    
     In other words, `nums_list` is a 2D, k by k list

  The function alters the list so that the element at nums_list[i][j]
    is swapped with nums_list[j][i]


  """





def sum22while(nums):
  """
  sum22while takes a list of integers and returns true if there
  are two consecutive twos in nums

  In this version, you can only use a while loop and the list function

  nums.pop()

  which will remove the last element of the list


>>> sum22while([2])
False
>>> sum22while([2,2])
True
>>> sum22while([2,3,2])
False
>>> sum22while([3,2,2,3])
True
>>> sum22while([1,2,3,4,5,2,2])
True
  """





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


if __name__ == "__main__":
    runalltests()
