# DO NOT ALTER THIS CODE
import random

#################################################################
#   CS161 S15  -  Instructor: David Baldwin (dbaldwin@pdx.edu)
#   Homework #2
#   Version 0.1: 4-27-2015
#
#   INTRODUCTION:
#
#   In class, we have been talking about how to model a bingo game 
#   using data structures. We will implement some of the functions 
#   for the bingo game below
#
#   In Part I, you'll implement a few simple functions to map bingo
#    characters to list elements.  In Part II, you'll use
#    multidimensional lists to check whether a bingo card is complete.
#    In part III, you'll read and understand how to make the bingo
#    game work with our data structure
#
#   Recall from class that a bingo card consists of two 5 by 5 lists,
#   the `bingo card` and the `mark sheet`.  The `bingo card` contains
#   the integers to be matched when a ball is pulled from the machine. The
#   `mark sheet` keeps track of whether we have marked the sheet
#
#   CONTENTS/RUBRIC:
#   
#   Part I (15 points)
#      a)  7.5 points
#      b)  7.5 points 
#   Part II (55 points)
#      a-e) 10 points each 
#      f) 5 points
#   Part III (30 points + 30 extra credit) 
#      a) 30 points
#      b) 30 points EXTRA CREDIT
#
#   You should work to maximize the number of points you might receive
#       but keep in mind that grades will be scaled.  Partial credit will
#       be given based on how close you are to a working, correct solution 
#       (not the number of tests passed)
#       
#
#   SUBMISSION INSTRUCTIONS:
#
#   Write you name in the comment below
# 
#      YOUR NAME HERE
#
#   Submit this file via the D2L Dropbox.  Remember to run the tests
#   before you submit to catch any errors.  Remember that submitting 
#   any part of this or any homework not written by you is a violation 
#   of the PSU Code of Conduct

cs161autoruntests = True
# PART I
# a)

def map_bingochar_to_column(bingochar):
    """ map_bingochar_to_column takes an single character string column
    and returns the the column associated with that bingo string

    There are several ways to do this, you can use an 'if', a dictionary
    mapping characters to columns or there is also a list method you might use


>>> map_bingochar_to_column("B")
0
>>> map_bingochar_to_column("I")
1
>>> map_bingochar_to_column("N")
2
>>> map_bingochar_to_column("G")
3
>>> map_bingochar_to_column("O")
4
    """

    col= []
    if bingochar == "B":
        col = [0]
    if bingochar == "I":
        col = [1]
    if bingochar == "N":
        col = [2]
    if bingochar == "G":
        col = [3]
    if bingochar == "O":
        col = [4]
    #else:
        #print("Not a BINGO Character")
    return col

# b)

def map_number_to_bingochar(number):
    """ map_column_to_bingochar takes an integer number
    and returns the the bingo character associated with
    that number

    The (inclusive) ranges are as follows
    B: 1-15 
    I: 16-30 
    N: 31-45 
    G: 46-60
    O: 61-75

    There are several ways to do this, you can use an 'if' to test ranges or you can
    use a dictionary.  If you do the latter, you have to convert `number` to a column
    (HINT: There are 15 possible numbers in each column, you cna use // to do the
    conversion) and then map from column number to column letter

>>> map_number_to_bingochar(0)
'O'
>>> map_number_to_bingochar(1)
'B'
>>> map_number_to_bingochar(15)
'B'
>>> map_number_to_bingochar(16)
'I'
>>> map_number_to_bingochar(30)
'I'
>>> map_number_to_bingochar(31)
'N'
>>> map_number_to_bingochar(45)
'N'
>>> map_number_to_bingochar(46)
'G'
>>> map_number_to_bingochar(56)
'G'
>>> map_number_to_bingochar(61)
'O'
>>> map_number_to_bingochar(75)
'O'
    """
    i=0
    start = [1,16,31,46,61,76]
    if number > 0 and number < 16:
        i = "B"
    if number > 15 and number < 31:
        i = "I"
    if number > 30 and number < 46:
        i = "N"
    if number > 45 and number < 61:
        i = "G"
    if number > 60 and number < 75:
        i = "O"
    return i
    
    
    




# Part II
# Below are 6 test marksheets for the next problems

# Nothing is finished
testcard0 = ( [False,False,False,False,False],
              [False,False,False,True,False],
              [False,False,False,True,False],
              [False,False,False,True,False],
              [False,False,False,True,False])


# Complete row
testcard1 = ( [False,False,False,True,False],
              [False,False,False,True,False],
              [False,False,False,True,False],
              [False,False,False,True,False],
              [False,False,False,True,False])

# Complete column
testcard2 = ( [False,False,False,False,False],
              [False,False,False,False,False],
              [True,True,True,True,True],
              [False,False,False,False,False],
              [False,False,False,False,False])

# Complete diagonal
testcard3 = ( [True,False,False,True,False],
              [False,True,False,False,False],
              [False,False,True,False,False],
              [False,False,False,True,False],
              [False,False,False,False,True])

# Complete diagonal
testcard4 = ( [False,False,False,True,True],
              [False,False,False,True,False],
              [False,False,True,False,False],
              [False,True,False,False,False],
              [True,False,False,False,False])

# Complete 4 corners
testcard5 = ( [True,False,False,False,True],
              [False,False,False,False,False],
              [False,False,False,False,False],
              [False,False,False,False,False],
              [True,False,False,False,True])


# a)
def is_card_complete_column(bingomarks):
    """ is_card_complete_column takes in a mark sheet `bingomarks`
        and returns true if there is a column with all True values
>>> is_card_complete_column(testcard1)
False
>>> is_card_complete_column(testcard2)
True
>>> is_card_complete_column(testcard3)
False
>>> is_card_complete_column(testcard4)
False
>>> is_card_complete_column(testcard5)
False


    """
    for i in range(5):
        count = 0
        for j in range (5):
            if bingomarks[i][j] == True:
                count += 1
        if (count == 5):
            return True
    return False


# b)
def is_card_complete_row(bingomarks):

    """ is_card_complete_row takes in a mark sheet `bingomarks`
        and returns true if there is a row with all True values

>>> is_card_complete_row(testcard1)
True
>>> is_card_complete_row(testcard2)
False
>>> is_card_complete_row(testcard3)
False
>>> is_card_complete_row(testcard4)
False
>>> is_card_complete_row(testcard5)
False

    """

    for i in range(5):
        count = 0
        for j in range (5):
            if bingomarks[j][i] == True:
                count += 1
        if (count == 5):
            return True
    return False

# c)
def is_card_complete_diagonal1(bingomarks):
    """ is_card_complete_diagonal1 takes in a mark sheet `bingomarks`
        and returns true if there if the diagonal starting at the top left
        corner and ending at the bottom right corner are all True

>>> is_card_complete_diagonal1(testcard1)
False
>>> is_card_complete_diagonal1(testcard2)
False
>>> is_card_complete_diagonal1(testcard3)
True
>>> is_card_complete_diagonal1(testcard4)
False
>>> is_card_complete_diagonal1(testcard5)
False
        
    """
    count = 0
    for i in range(5):
        if bingomarks[i][i] == True:
                count += 1
        if (count == 5):
            return True
    return False

# d)
def is_card_complete_diagonal2(bingomarks):

    """ is_card_complete_diagonal2 takes in a mark sheet `bingomarks`
        and returns true if there if the diagonal starting at the top right
        corner and ending at the bottom left corner are all True

>>> is_card_complete_diagonal2(testcard1)
False
>>> is_card_complete_diagonal2(testcard2)
False
>>> is_card_complete_diagonal2(testcard3)
False
>>> is_card_complete_diagonal2(testcard4)
True
>>> is_card_complete_diagonal2(testcard5)
False

    """
    count = 0
    for i in range(5):
        if bingomarks[i][4-i] == True:
                count += 1
        if (count == 5):
            return True
    return False

# e)
def is_card_complete_fourcorners(bingomarks):
    """ is_card_complete_fourcorners takes in a mark sheet `bingomarks`
        and returns true if all of the following are true

        1) The top left corner is marked
        2) The bottom right corner is marked
        3) The top right corner is marked
        4) the bottom left corner is marked

>>> is_card_complete_fourcorners(testcard1)
False
>>> is_card_complete_fourcorners(testcard2)
False
>>> is_card_complete_fourcorners(testcard3)
False
>>> is_card_complete_fourcorners(testcard4)
False
>>> is_card_complete_fourcorners(testcard5)
True


    """
    for i in range (5):
        for j in range (5):
            if (bingomarks[0][0] == True) and (bingomarks [0][4] == True) and (bingomarks [4][0] == True) and (bingomarks [4][4] == True):
                return True
    return False
    
# f)
def is_card_complete(bingomarks):
    """ is_card_complete returns true if ANY of the above is_card_complete....
        return True
>>> is_card_complete(testcard1)
True
>>> is_card_complete(testcard2)
True
>>> is_card_complete(testcard3)
True
>>> is_card_complete(testcard4)
True
>>> is_card_complete(testcard5)
True
>>> is_card_complete(testcard0)
False

    """
    if is_card_complete_column(bingomarks)==True or is_card_complete_row(bingomarks)==True or is_card_complete_diagonal1(bingomarks)==True or is_card_complete_diagonal2(bingomarks)==True or is_card_complete_fourcorners(bingomarks)==True:
        return True
    return False
    
    





# PART III
# a)
#  Below is the play_bingo function.  It plays bingo with a single player.  Your task is to understand
#    how it works and implement the mark_card function so that both mark_card and play_bingo pass the tests
#
#  DO NOT change play_bingo.  Until you implement mark_card, play_bingo will fail the tests

def play_bingo(callorder):
    """ play_bingo takes a callorder and returns the turn when the bingo game
        terminates (when one player is done)

>>> play_bingo(initialize_callorder(125))
30
>>> play_bingo(initialize_callorder(12043))
50
>>> play_bingo(initialize_callorder(0))
54
>>> play_bingo(initialize_callorder(3))
30
>>> play_bingo(initialize_callorder(5))
48
>>> play_bingo(initialize_callorder(10))
22
    """
    bingocard = create_bingo_card()
    marks     = create_blank_cover()
    turn = 1
    while len(callorder):
        call = next_call(callorder)
        mark_card(call,bingocard,marks)

        # uncomment to debug
        #print_card(bingocard,marks)

        if is_card_complete(marks): 
            break

        turn += 1
        
    return turn



def mark_card(call,bingocard,bingomarks):
    """ mark_card takes a tuple `call`, a bingo card `bingocard` and a mark sheet `marks`. IT returns a
        boolean indicating whether or not the sheet was marked.

        If the square indicated by the `call` tuple is present in the card, it sets the corresponding
        mark sheet value to True and returns True

        If the square doesn't exist, it returns False

Create some test data
>>> card = create_bingo_card(1234)
>>> marks = create_blank_cover()

Calling print_card(card,marks) prints
B	I	N	G	O

13	30	42	46	71
8	28	32	60	70
2	25	44	58	68
1	16	36	59	74
15	26	34	51	73


Now mark the top row
>>> mark_card(("B",13),card,marks)
True
>>> marks
([True, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False])

Whoops, there's no "B-25"
>>> mark_card(("B",25),card,marks)
False



>>> mark_card(("I",30),card,marks)
True
>>> mark_card(("N",42),card,marks)
True
>>> mark_card(("G",46),card,marks)
True
>>> mark_card(("O",71),card,marks)
True
>>> is_card_complete(marks)
True


Calling print_card(card,marks) prints
____________________________________
B	I	N	G	O

X	X	X	X	X
8	28	32	60	70
2	25	44	58	68
1	16	36	59	74
15	26	34	51	73

    """
    
    k= map_bingochar_to_column(call[0])
    for i in range (5):
        if (bingocard[k][i]==call[1]):
            bingomarks[k][i]=True
            return True
    return False
    # 1) access the tuple `call` and get the bingocharacter
    # 2) transform that bingocharacter into a column number from 0-4 inclusive (use your map_bingochar_to_column function)
    # 3) use the column number to access the column list in `bingocard` that *might* contain the number in `call`
    #    , keeping track of the row number where it is found
    # 4) if the number does not exist in the `bingocard` return False
    # 5) otherwise, set the boolean value at the same row and column in `bingomarks` to True and return True




# Part IV
# Extra Credit
# 
# Copy the play_bingo function into a new function
# play_bingo_multi that takes an additional integer
# parameter `players` indicating how many players are
# playing.  Simulate the Bingo game and return a tuple
# (winner,step). `winner` is the zero based integer 
# representing the player who `won`. If two players
# win at the same time, the lowest number is returned.
# `step` is the step at which the game ended
def play_bingo_multi(callorder, players):

    pass







# helper functions
# DO NOT MODIFY
def next_call(callorder):
    '''takes a list of uncalled numbers and returns a tuple (c, n), where n is a number in the range 1-75.

    c is a letter from BINGO that indicates the column of the bingo card in which
    n might be found.
    '''
    # 1) remove a tuple from call order and assign it to a variable
    to_call = callorder.pop(0)

    # 2) return that tuple
    return to_call

def create_bingo_card(theseed):
    '''Create and return a new bingocard given an integer `theseed`. Each
    distinct integer will generate a distinct bingocard

    The card is represented as a 5-tuple of lists.  Each list contains
    5 numbers chosen at pseudo-random from the appropriate range:
    [1..15] for the first, [16..30] for the second, â€¦ and [60..75] for the last.

    '''
    r = random.Random();
    r.seed(theseed)

    bColumn = (r.sample(range(1,16),5))
    iColumn = (r.sample(range(16,31),5))
    nColumn = (r.sample(range(31,46),5))
    gColumn = (r.sample(range(46,61),5))
    oColumn = (r.sample(range(61,76),5))
    return (bColumn, iColumn, nColumn, gColumn, oColumn)

def create_blank_cover():
   '''Return a blank cover for a bingo card.

   A blank cover is a 5-tuple of lists; each list contains 5 elemenst, all False.
   '''
   col = [False, False, False, False, False]
   return(list(col), list(col), list(col), list(col), list(col))

def print_card(bingocard,bingomarks):
    '''card and covered are both 5-tuples of lists.  Each list is of length 5.

    The lists in the card tuple contain numbers, representing the columns
    of numbers on a bingo card.  The lists in the covered tuple are booleans;
    True means that the corresponding number has been covered.
    This function prints a textual representation of the Bingo card, with
    X's replacing the covered numbers.
    '''
    bList, iList, nList, gList, oList = bingocard
    bCov, iCov, nCov, gCov, oCov = bingomarks
    print('_' * 36)
    print('B\tI\tN\tG\tO\n')
    for i in range(5):
        bItem = 'X' if bCov[i] else bList[i]
        iItem = 'X' if iCov[i] else iList[i]
        nItem = 'X' if nCov[i] else nList[i]
        gItem = 'X' if gCov[i] else gList[i]
        oItem = 'X' if oCov[i] else oList[i]
        print(bItem, iItem, nItem, gItem, oItem, sep='\t')



def initialize_callorder(s=1):
    '''Initialize the set of numbers to be called

    This should be called before starting a new game of bingo.
    '''
    
    r = random.Random(s)
    uncalledNumbers = list(range(1,76))
    permutation = r.sample(uncalledNumbers,len(uncalledNumbers))
    permutation_bingo = []
    for n in permutation:
        tp = (map_number_to_bingochar(n),n)
        permutation_bingo.append(tp)
    return permutation_bingo

