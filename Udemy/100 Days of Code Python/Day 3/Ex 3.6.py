print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
lr = input('''As you land on the lsland you see two paths before you. Do you choose the left path that seems to 
have been traveled or the right path that leads into dense bushes?\n ''').lower()

if lr == 'right' or lr =='r':
    sw = input('''As you make your way thorugh the thick underbrush a raging river appears before you... 
    Do you wait to see if the river will calm or do you attempt to swim throught the raging waters?\n''').lower()

    if sw == 'wait' or sw =='w':
        rby = input('''The waters calm as night begins to set in and you make your way across. 
        through the woods to find a clearing with three doors in the middle of the clearing. 
        One red door, one blue door, and one yellow door. Which door do you choose to open?\n''').lower()

        if rby == 'yellow' or rby =='y':
            print('You Win!')
        else:
            print('A monster erupts from the door and makes you their next meal... Game Over!')
    else:
            print('The rapid waters carry you to a waterfall were you are impaled by rocks when you land... Game Over!')
else:
            print('You wander around aimlessly for days before you die of hunger... Game Over!')