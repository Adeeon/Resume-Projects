# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

cmonths = age_int * 12
cweeks = age_int * 52
cdays = age_int * 365

age_lim = 90

lim_month = age_lim * 12
lim_weeks = age_lim * 52
lim_days = age_lim * 365

rem_month = lim_month - cmonths
rem_weeks = lim_weeks - cweeks
rem_days = lim_days - cdays

print(f'You have {rem_days} days, {rem_weeks} weeks, and {rem_month} months left.')