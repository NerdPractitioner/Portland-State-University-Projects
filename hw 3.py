# In this assignment, you will implement a game of tic-tac-toe. If you
# are unfamiliar with the game, please see 
# 
#  http://en.wikipedia.org/wiki/Tic-tac-toe
#
# In this assignment, you are responsible for writing your own code. 
# it is highly suggested you write doctests, but not required. The only
# code provided is a function called main that should serve as the entry
# point into your game.  You are, of course, welcome to define new classes
# and functions (and if you're not, you may want to reconsider your design!).
# You may also import any module we have used in class (e.g., random)
#
# Your score will be out of 100. There are a total of 190 possible
# points. Your grade will be up to 130/100.  You are required to
# complete #1 and #8 to pass the assignment, but are otherwise free to choose
# which parts of the homework you work on. You are allowed to reuse
# any code from the book but please cite what you reuse. 
#
# 1. ---  Basic tic-tac-toe implementation (50 points, REQUIRED)
# 2. ---  Two player tic-tac-toe with player input (25 points)
# 3. ---  Object-oriented TicTacToe  (up to 20 points) 
# 4. ---  Write a function to have the computer pick a square  (30+10)
# 5. ---  N by N tic tac toe (20 points)
# 6. --- K player tic-tac-toe (20 points)
# 7. --- Style points (0-10)
# 8. --- Write-up (10 points, REQUIRED)

#1.---  Basic tic-tac-toe implementation (50 points, REQUIRED)
#    
#  The requirements for the basic tic-tac-toe game is as follows
#  
#  1) Appropriate data structures for the game of tic-tac-toe
#  2) A method or function to change the mark on the tic-tac-toe grid
#  3) A method or function to determine the winner of the game ("X", "O" or 
#        "DRAW"). 
#  4) A method to display the tic-tac-toe board via print(), for example
#  5) No use of global variables
#
#-------
#| X O |
#| XXO |
#|  OX |
#-------
#
#2. ---  Two player tic-tac-toe with player input (25 points)
# 
#  Create a method that allows two users to play tic-tac-toe.  Each player
#  will make a move via input() and the result of the move will be shown via
#  print.  For example
#
# X please input your row:0
# X please input your column:0
# -------
# | X   |
# |     |
# |     |
# -------
# O please input your row:2
# O please input your column:2
# -------
# | X   |
# |     |
# |   O |
# -------
# X please input your row:0
# X please input your column:1
# -------
# | XX  |
# |     |
# |   O |
# -------
# O please input your row:2
# O please input your column:1
# -------
# | XX  |
# |     |
# |  OO |
# -------
# X please input your row:0
# X please input your column:2
# -------
# | XXX |
# |     |
# |  OO |
# -------
# X  is the winner
#
#3. ---  Object-oriented TicTacToe  (up to 20 points) 
#
#  Write you tic-tac-toe game and methods in a class called TicTacToeGame. 
#    Appropriate use of class/object features will gain you more points
#
#4. ---  Write a function to have the computer pick a square  
#                  (up to 30 points + 10  for interface) 
#  
#  Develop a function that marks a  square for a given player. The more 
#   creative you are, the more points you will receive.  Choosing a 
#   random empty square will net you more points than choosing the first 
#   open square.  Developing a more intelligent strategy will gain you
#   more than both of these. Be sure to write comments explaining your 
#   function if the strategy is not apparent from the code.
#
# For 10 additional points, write an function that allows the user to play
#    against the computer or lets two computers duke it out.
#
#5. ---  N by N tic tac toe (20 points)
#  
#  Allow the programmer to specify `n` to create an n by n tic-tac-toe grid. 
#    and adapt your functions to the new data structure.
#
#6. --- K player tic-tac-toe (20 points)
#
#  Allow the programmer to specify `k` to allow an arbitrary number (k>=1)
#    of players and adapt your functions to the new data structure.
#
#7. --- Style points (0-10)
#
#  Subjective extra points for clean code style 
#
#8. -- Writeup  (10 points REQUIRED)
# 
#   Include a summary of your project that includes the sections you
#   attempted and any notes on your design.  This need not be longer
#   than a paragraph or two - concisely explain what you attempted,
#   anything interesting you learned, where there is room for improvement,
#   etc.

# This is the entry point into your code

#create a blank card
def create_blank_card():
    """creates a blank card"""
    alist= []
    for i in range(3):
        alist.append([])
        for j in range(3):
            alist[i].append(False)
    return alist

#completion testing
def is_horizontal_complete(playerMarks):
    for i in range(3):
        count = 0
        for j in range(3):
            if playerMarks[i][j] == True:
                count+=1
        if (count == 3):
            return True
    return False

def is_vertical_complete(playerMarks):
        for i in range(3):
            count = 0
            for j in range (3):
                if playerMarks[j][i] == True:
                    count += 1
            if (count == 3):
                return True
        return False

def is_diagonal_complete(playerMarks):
    count = 0
    for i in range(3):
        if playerMarks[i][i] == True:
                count += 1
        if (count == 3):
            return True
    return False

def is_diagonal2_complete(playerMarks):
    count = 0
    for i in range(3):
        if playerMarks[i][2-i] == True:
                count += 1
        if (count == 3):
            return True
    return False

def is_card_complete(playerMarks):
    if is_horizontal_complete(playerMarks)==True or is_vertical_complete(playerMarks)==True or is_diagonal_complete(playerMarks)==True or is_diagonal2_complete(playerMarks)==True:
        return True
    return False

# Create Player Card

def create_player_card():
    row = [False, False, False]
    return(list(row), list(row), list(row))

def get_player_input(player):
    mark = input("player "+ player +" please pick the row and column from 0 to 2 to replace a False with your mark ex.(0,1)")
    return mark

def switch_turn(turn):
    if turn==player1:
        return player2
    elif turn==player2:
        return player1
    return

def switch_player(player):
    if player=="1":
        return "2"
    elif player=="2":
        return "1"
    return

# Game functionallity           
def main():                
    game_card = create_blank_card()
    print(game_card)
    player1=create_player_card()
    print(player1)
    player2=create_player_card()
    turn=player1
    player="1"
    outcome = "Cat's game!"
    while not is_card_complete(player1)==True or is_card_complete(player2)==True:
        if turn == player1:
            mark=get_player_input(player)
            a,b=mark
            player1[a][b]=True
            game_card[a][b]="x"
            
        elif turn ==player2:
            mark=get_player_input(player)
            a,b=mark
            player2[a][b]=True
            game_card[a][b]="o"
        print(game_card)
        turn=switch_turn(turn)
        switch_player(player)
    outcome=("Player " + player + " wins!")
    return print(outcome)



# For this assignment, I tried to modify some of the code from our bingo game.
# I would probably try more like the book did if I were to do this again, for instance,
# allowing the player to pick from 0 to 8 instead of expecting a tupole. I had problems
# all along the way and I ran out of time today but I feel like i was getting close. I
# hope that I can at least get some partial credit for this.

# I felt using a class would have made this a lot easier but I didn't feel confident enough
# with the new class content we learned yet. When I stopped; I was getting an error that there
# were too many values to unpack from a,b=mark where I was asking for a tupole.

# My overall goal was to make a card to be shown and to make player cards to be checked individually.
# I wasn't able to get the card to display in the shape of a tic-tac-toe board to the players. Nor was I
# able to fill it with anything but False without crashing my shell. I planned to take the player's tuple
# and map it to the player's card and the game card. I believe that if got my program to accept player 
# input properly that it would have switched players each while loop and printed the player whose turn
# it was when one of the while conditions were met.

# I also realize my game wouldn't work if there was a tie at this point but couldn't figure out where to
# put a condition to fix that.



        

    
    
