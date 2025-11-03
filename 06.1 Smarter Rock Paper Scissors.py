## 6. Rock, Paper, Scissors
#**Functions needed:** `random.choice()`, `input()`
#**Concepts:** Lists, conditionals, comparison
#**Hints:** Create list of choices, get computer's random choice, compare with user's choice using if/elif.

import random

# Definition
choice = ['Rock', 'Paper', 'Scissors'] #what are the differences between '' and ""

# Introduction
print(f"Hello and welcome to Sashymi's 100 Codes! Today we will play a better Rock Paper Scissors! With enhanced codes! And better logic!")

# Game starts
while True:

    # User plays
    userchoice = input("What is your play? (Rock/Paper/Scissors): ")

    # Checks for typo
    if userchoice not in choice:
        print("You have entered an invalid choice! Please try again!") # Using not in here is better than !=
        continue

    # Cpu plays
    cpuchoice = random.choice(choice)

    # Checks for tie
    if  userchoice == cpuchoice:
        print(f"You have played {userchoice}, while I played {cpuchoice}! Its a tie!")
        continue

    # Checks for winner
    if userchoice == "Rock" and cpuchoice == "Paper":
        print(f"You have played {userchoice}, while I played {cpuchoice}! Paper beats Rock! I win!")
    elif userchoice == "Rock" and cpuchoice == "Scissors":
        print(f"You have played {userchoice}, while I played {cpuchoice}! Rock beats Scissors! I lose!")
    elif userchoice == "Paper" and cpuchoice == "Rock":
        print(f"You have played {userchoice}, while I played {cpuchoice}! Paper beats Rock! I win!")
    elif userchoice == "Paper" and cpuchoice == "Scissors":
        print(f"You have played {userchoice}, while I played {cpuchoice}! Scissors beat Paper! I lose!")
    elif userchoice == "Scissors" and cpuchoice == "Rock":
        print(f"You have played {userchoice}, while I played {cpuchoice}! Rock beats Scissors! I win!")
    elif userchoice == "Scissors" and cpuchoice == "Paper":
        print(f"You have played {userchoice}, while I played {cpuchoice}! Scissors beat Paper! I lose!")
    break

print("Thank you for the game! GG!")
