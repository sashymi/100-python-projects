## 6. Rock, Paper, Scissors
#**Functions needed:** `random.choice()`, `input()`
#**Concepts:** Lists, conditionals, comparison
#**Hints:** Create list of choices, get computer's random choice, compare with user's choice using if/elif.

# Planning stage - looks simple enough, start with import random, then ask for input, then decide on what to play (randomly :p), then compare between input and computer's play, then outcome. if elif else for the choices, while to repeat if tie

import random
my_list=['Rock', 'Paper', 'Scissors']

print("Welcome to Sashymi's 100 Codes! Today we will play Rock, Paper, Scissors!")
user_choice = input("You will play (Rock/Paper/Scissors): ")
if user_choice not in my_list: #new function here! using not in for exclusions, if a typo, then please try again!
    print("I think there is a typo, I only accept exactly Rock, Paper or Scissors! Please try again!")
    exit()
cpu_choice = random.choice(my_list)

#tie=0                                   #tie has to be defined first. TIE CAN ALSO BE REMOVED ALTOGETHER
#if user_choice==cpu_choice: tie=1      #only then can tie be used here, and with operators =

while user_choice==cpu_choice: #tie==1:
    print(f"You played {user_choice}, and I played {cpu_choice}, it's a tie!")
    user_choice = input("You will play (Rock/Paper/Scissors): ")
    if user_choice not in my_list: #new function here! using not in for exclusions, if a typo, then please try again!
        print("I think there is a typo, I only accept exactly Rock, Paper or Scissors! Please try again!")
    exit()
    cpu_choice = random.choice(my_list)
    if user_choice!=cpu_choice: break #tie=0   # break here or tie==0? lets try both. both works. BUT tie=0 MUST be used. we ASSIGN the zero to the tie, and not compare it to the zero.

while user_choice!=cpu_choice: #tie==0:
    if user_choice == "Rock" and cpu_choice == "Paper":
        print(f"You played {user_choice}, and I played {cpu_choice}, I win!")
        break
    elif user_choice == "Rock" and cpu_choice == "Scissors":
        print(f"You played {user_choice}, and I played {cpu_choice}, I lose :(")
        break
    elif user_choice == "Paper" and cpu_choice == "Scissors":
        print(f"You played {user_choice}, and I played {cpu_choice}, I win!")
        break
    elif user_choice == "Paper" and cpu_choice == "Rock":
        print(f"You played {user_choice}, and I played {cpu_choice}, I lose :(")
        break
    elif user_choice == "Scissors" and cpu_choice == "Paper":
        print(f"You played {user_choice}, and I played {cpu_choice}, I lose :(")
        break
    elif user_choice == "Scissors" and cpu_choice == "Rock":
        print(f"You played {user_choice}, and I played {cpu_choice}, I win!")
        break

print("Thanks for the game! GG!")

# What have I learned?
# this is quite complex.. I never knew coding such a simple program can be this complex
# i feel like the culmination of good practices and coding hygiene can affect me in the long run
# 1. it is good for while loops to be paired with if, elif and else loops.
# 2. for error handling, in case the user typos, we can use 'in' or 'not in' functions
# 3. i first start out with a variable tie. if tie is 0, then there will be a conclusion, if tie is 1, then its a bit complex, where the program will have to keep playing untuk its not tie
# 4. gpt pointed out that we dont have to use tie variable, we could simply just while user_choice == cpu_choice, which simplifies things
# 5. i learned that indentations are important.. where you break and where you exit() also plays a role in exiting your while loops etc
# 6. finally, the typo handling could definitely be done in a better way.. i feel like its too rigid. as of now, everytime the user is asked for an input, the typo handler will come to the rescue.
# once at the start of the initial game, 2nd at the while loop if the game is a tie..