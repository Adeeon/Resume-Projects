# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('red', 'green')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# py -m pip install prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemone Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'


print(table)