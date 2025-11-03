## 5. Number Guessing Game
#**Functions needed:** 'import random' `random.randint()`, `input()`, `int()`
#**Concepts:** While loops, conditionals, comparison operators
#**Hints:** Generate random number, use while loop until correct guess, give "too high/too low" feedback.

# we will guess 1-10 for a faster game, then we will try 1-100
# idea is the user thinks of a number, then guess, then input either high or low, then guess again, until correct, using while loop

import random

#intro
print("Hi, today on Sashymi's 100 programs, we will try a Number Guessing Game! I will guess the number in your mind from 1-100!")

#assigning min and max values to a variable
min = int(1)
max = int(100)

#initial random number
number = random.randint(min,max) #comma , not a dash -
print(f"Your number is {number}!")

#case where first guess was correct
highlow = input ("How did I do, is your number higher or lower? (correct/higher/lower): ")

# encapsulate all with while, then use if elif else for conditions
while highlow != "correct": # looping everything in while, while not correct, repeat until correct

    if highlow == "higher":
        min = number
        number = min+((max-min)//2)
        print(f"Your number is {number}!")
        highlow = input ("How did I do, is your number higher or lower? (correct/higher/lower): ")

    elif highlow == "lower":
        max = number
        number = max-((max-min)//2)
        print(f"Your number is {number}!")
        highlow = input ("How did I do, is your number higher or lower? (correct/higher/lower): ")

    elif highlow != "higher" and highlow != "lower" and highlow != "correct":
        print("Invalid operation! Please check your inputs!")
        break
        

if highlow == "correct": print(f"We successfully guessed your number! It is {number}! GG and thank you!")
else: print("Something went wrong, thanks for playing!")

# What have I learned?
# Coding is not easy LMAO
# a good way to use while, is to use while, if, elif, else: altogether! dont be confused and use nested whiles, just use 1 while, and nested if else, then it will all make sense
# // vs /, where // will return an integer, whereas / will return a float with decimals
# the mathematics of this is very confusing, but once i have gotten it, its quite easy, instead of using number variable, we use max and min instead, and to ensure that the new max and new min does not go out of bounds,
# the formula (max-min)//2 is very reassuring. as it converges all the way into 1 answer
# 2 ways to get out of a while - being 1. break which gets out altogether, and 2. continue, which skips the current interation in the while and moves on to the next iteration, which is not needed in this code
# avoid using min or max as variable, as they are built in functions

# IMPROVEMENTS:
#   to start guessing at exactly middle of range, for truly efficient BINARY SEARCH 
#   to introduce a new variable, guesses, for total number of guesses, and guess+=1 as the first function in the while loop
# if feedback == "higher":
#        min_num = number + 1  # +1 to avoid guessing the same number
#   elif feedback == "lower":
#        max_num = number - 1  # -1 to avoid guessing the same number
#   above function can be used to include the 1 and 100 into the guesses