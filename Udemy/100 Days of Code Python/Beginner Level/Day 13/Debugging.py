############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21): # for i in range(1, 20) i never tru199ly = 20 because of how range works
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # randint(1, 6) list index out of range for 6
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: # 1994 would terminate and the if/elif need a >= to run properly.
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?")) # not an int orginaly but a string
# if age > 18:
#   print(f"You can drive at age {age}.") # wasn't an f{string}

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # == not = so it was comparing and not manipulating.
# print(pages, word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#       new_item = item * 2
#       b_list.append(new_item) # b_list.append(new_item) was not spaced into the for loop and would only add the last new_item
#   print(b_list)

# mutate([1,2,3,5,8,13])