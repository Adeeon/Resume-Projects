rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
rps = [rock, paper, scissors]
player = input('Select rock, paper or scissors.\n')
com = random.randint(0, (len(rps)-1))
complay = rps[com]
status = True
while status:
    if player == 'rock':
        player = rock
        print(f'Player chose:\n {player}')
        print(f'Computer chose:\n {complay}')
        if player == complay:
            print('Its a draw')
        elif com == 1:
            print('You lose.')
        else:
            print('You Win.')

    if player == 'paper':
        player = paper
        print(f'Player chose:\n {player}')
        print(f'Computer chose:\n {complay}')
        if player == complay:
            print('Its a draw')
        elif com == 2:
            print('You lose.')
        else:
            print('You Win.')

    if player == 'scissors':
        player = scissors
        print(f'Player chose:\n {player}')
        print(f'Computer chose:\n {complay}')
        if player == complay:
            print('Its a draw')
        elif com == 0:
            print('You lose.')
        else:
            print('You Win.')
        
    if player != 'sissors' or player != 'rock' or player != 'paper':
        print('Invalid input. Please try again.')
    