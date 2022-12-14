# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.



# Here are the numbers up to 100, prime numbers are highlighted in yellow:



# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.
# Hint
# Remember the modulus:
# https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python

# Make sure you name your function/parameters the same as when it's called on the last line of code.

# Use the same wording as the Example Outputs to make sure the tests pass.

# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

#Write your code below this line ๐
def prime_checker(number):
    prime = 0
    for i in range(1, 101):
        if number % i == 0:
            prime += 1
    if prime == 2:
        return print("It's a prime number.")
    else:
        return print("It's not a prime number.")



#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)