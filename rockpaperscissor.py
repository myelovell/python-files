# My E. Lovell 2019-03-08, sten sax påse, 2 player

import sys

player1 = input("enter player one name:\n")
player2 = input("enter player two name:\n")

player1_input = input("%s, player one, time to chose play: rock, paper or scissor?:\n" %player1)
player2_input = input("%s, player two, time to chose play: rock, paper or scissor?:\n" %player2)

def compare(player1, player2):
    if player1_input == player2_input:
        return ("it's a tie")

    elif player1_input == 'rock':
        if player2_input == 'scissor':
            return ("rock wins! ", player1, "gets 1 point")

    elif player1_input == 'rock':
        if player2_input == 'paper':
            return ("paper wins! ", player2, "gets 1 point")

    elif player1_input == 'paper':
        if player2_input == 'rock':
            return ("paper wins! ", player1, "gets 1 point")

    elif player1_input == 'paper':
        if player2_input == 'scissor':
            return ("scissor wins! ", player2, " gets 1 point")

    elif player1_input == 'scissor':
        if player2_input == 'paper':
            return ("scissor wins! ", player1, " player 1 gets 1 point")

    elif player1_input == 'scissor':
        if player2_input == 'rock':
            return ("rock wins! ", player2, " gets 1 point")
    else:
        return ("invalid play, you did not enter: rock, paper nor scissor")
        sys.exit()

print(compare(player1_input, player2_input))

    #rock < paper, rock > scissor
    #paper < scissor, paper > rock
    #scissor < rock, scissor > paper

    #currently not working
