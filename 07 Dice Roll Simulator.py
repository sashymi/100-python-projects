## 7. Dice Roll Simulator
#**Functions needed:** `random.randint()`
#**Concepts:** Random number generation
#**Hints:** Use randint(1,6) for one die, call it twice for two dice, add results.

"""
Planning
input: user input how many dice they want to use, x
process: while x=0, roll dice, x+1, continue
edge cases: misinput / input is not an int()

usually edge cases are only for math operations (divide zero) or mostly from user input, since that is a variable that we cannot control. lets start!
"""
import random
dicecount = 1
dicevalue = 0

# Introduction
print("Hello and welcome to Sashymi's 100 codes! Our program today will be a Super Dice Roller!")

# User input & input validation combined
try:
    dicemax = int(input("To start, please specify how many dice(s) you wish to use!: "))
except ValueError:
    print("Your input is not an integer! Please try again!")
    exit()

# Processing
while dicecount <= dicemax:
    diceroll = random.randint(1,6) # Coder is able to change how many faces the dices have
    print(f"Dice number {dicecount} has rolled a {diceroll}!")
    dicecount += 1
    dicevalue += diceroll
    
# Results
print(f"The rolls have ended! You have rolled a total of {dicemax} time(s), and have attained a total value of {dicevalue}! Thank you for playing!")

# What I have learned
# If you are expected an integer input, it is better to define the input straightaway as int
# operators to compare between current value and max value, <= is more helpful than !=
