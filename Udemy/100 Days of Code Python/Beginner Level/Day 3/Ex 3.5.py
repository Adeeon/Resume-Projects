# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_score = lower_name1.count('t') + lower_name2.count('t')
r_score = lower_name1.count('r') + lower_name2.count('r')
u_score = lower_name1.count('u') + lower_name2.count('u')
e_score = lower_name1.count('e') + lower_name2.count('e')

true_score = t_score + r_score + u_score + e_score
true_score = str(true_score)

l_score = lower_name1.count('l') + lower_name2.count('l')
o_score = lower_name1.count('o') + lower_name2.count('o')
v_score = lower_name1.count('v') + lower_name2.count('v')
e_score = lower_name1.count('e') + lower_name2.count('e')

love_score = l_score + o_score + v_score + e_score
love_score = str(love_score)

Score = true_score + love_score
Score = int(Score)

if Score < 10 or Score > 90:
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif Score >= 40 and Score <= 50:
    print(f'Your score is {Score}, you are alright together.')
else:
    print(f'Your score is {Score}.')


