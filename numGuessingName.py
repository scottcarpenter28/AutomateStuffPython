import random
import sys

playAgain = True
while playAgain:
    ran = random.randint(1, 20)
    print('Guess a number between 1 and 20')
    guess = 0
    attempts = 0

    while guess != ran:
        guess = int(input())
        if guess < ran:
            print('Higher')
        elif guess>ran:
            print('lower')
        else:
            print('Correct!')
        attempts =attempts +1
    print('It took '+str(attempts)+' attempts to answer. Enter Y to play again, or any key to exit.')
    again = input()
    if again =='y':
        continue
    else:
        sys.exit()
