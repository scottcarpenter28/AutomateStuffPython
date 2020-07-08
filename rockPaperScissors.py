import system
import random

playAgain = True
win =0
lose =0
tie =0
while playAgain:
    print('Enter r for rock, p for paper, and s for scissors')
    playerIn = input()
    ran = random.randint(1,3)

    if playerIn == 'r':
        playerIn = 1
    elif playerIn =='p':
        playerIn = 2
    elif playerIn == 's':
        playerIn = 3
    else:
        print("Enter a valid letter")

    if playerIn < ran:
        print('You Lose')
        lose =lose+1
    elif playerIn > ran:
        print('You win')
        win = win+1
    else:
        print('Its a tie')
        tie = tie+1

    comp =''
    if ran == 1:
        comp = 'r'
    elif playerIn ==2:
        comp = 'p'
    else:
        comp = 's'
