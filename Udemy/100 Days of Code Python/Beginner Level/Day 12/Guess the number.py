#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

Dif = input('''Welcome to the Number Guessing Game!\n
I'm thinking of a number between 1 and 100.\n
Choose a difficulty. Type "easy" or "hard": ''')

if Dif == 'easy':
    lives = 10
elif Dif == 'hard':
    lives = 5
else:
    print('Your did not choose a difficulty correctly closing.') 

rando = random.choice(range(1,101))


while lives >= 0:
    print(f'You have {lives} attempts remaining to guess the number.')
    Choice = int(input(f'Make a guess: '))
    if Choice > rando:
        print('Too high.\nGuess again.')
        lives -= 1
    elif Choice < rando:
        print('Too low.\nGuess again.')
        lives -= 1
    elif lives == 0:
        print(f'You ran out of lives the random number was {rando}.')
        lives -= 1
    elif Choice == rando:
        print(f'You guessed {Choice} and the random number was {rando}.')
        lives = 0
