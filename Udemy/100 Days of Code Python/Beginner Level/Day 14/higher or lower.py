from random import randint
from data import data
from art import logo, vs
import os

a = data[randint(0, len(data)-1)]

score = 0

fail = False
game = True
while game: 
    
    # start the game and set a base winner incase of a wrong choice
    winner = ''
    
    while not fail:
        
        #start the loop and set random challenger to compare against
        b = data[randint(0, len(data)-1)]
        #while challenger does equal contestant
        if b != a:
            
            #prints logo, score if not 0, vs, contestant and challenger
            print(logo)
            if score > 0:
                print(f"You'r right! Current score: {score}")
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
            print(vs)
            print(f'Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}')
            choice = input('Who has more follower? Type "A" or "B": ').upper()
            
            #checks for the correct choices to continue the game if right
            if a['follower_count'] > b['follower_count'] and choice == 'A':
                score += 1
                os.system('cls')
            #if b is the correct choice set a to be for the following runs
            elif a['follower_count'] < b['follower_count'] and choice == 'B':
                a = b
                score += 1
                os.system('cls')
            
            #fail states end the loop and assigns correct coice to winner
            else:
                if a['follower_count'] > b['follower_count']:
                    winner = a
                elif a['follower_count'] < b['follower_count']:
                    winner = b
                fail = True
                os.system('cls')
    
    #prints winner and sees if user wants to keep playing
    print(f'{winner["name"]} has more followers at {winner["follower_count"]} Million folloers.\nYour Final Score was {score}.')
    again = input('Would you like to try again? Type "y" or "n": ').lower()
    
    #resets loop if user wishs to keep playing.
    if again == 'y':
        score = 0
        fail = False
        os.system('cls')
    else:
        game = False

