# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# There are many ways of doing this. But to practice what we learnt in the last lesson, 
# you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# e.g. 1 means Heads 0 means Tails

# Example Output
# Heads
# or

# Tails
# When you're happy with your code, click submit.

# Testing Your Code
# Check your code is doing what it is supposed to. 
# When you're happy with your code, click submit to check your solution. 
# Your program may look like it is failing the tests when it isn't. 
# We're using the random functionality in this exercise, so the tests will match different outcomes.

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

flip = random.randint(1, 2)

if flip == 1:
    flip = 'Heads'
    print(flip)
elif flip == 2:
    flip = 'Tails'
    print(flip)