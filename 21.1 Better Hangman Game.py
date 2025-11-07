# 21. Hangman Game
#**Concepts:** While loops, strings, lists, conditionals
#**Hints:** Track guessed letters, display word with blanks, count wrong guesses, end after 6 wrong or word complete.
# 2nd try on hangman, 1st try was a disaster, doesnt help that i am tired i just wanna sleep man
# ok so proper planning this time
# think of main() first! then proceed to the functions! top down approach!

# 1. Get user input
# 2. Display words in underscores
# 3. While user is not winning or losing (_ is zero or guesses == 6)
# 4.    Show game state (current standing)
# 5.    Get guess
# 6.    Compare guess with all index of secret word
# 7.    if right, replace underscores with letter
# 7.    else: wrong guess
# 8.    show results - in main

def secretwordprompt():
    secretword = input("Gamemaster, please input your secret word: ")
    return secretword

def displayhidden(secretword):
    print(f"The length of your word is {len(secretword)}")
    print(f"Your word is {" ".join(("_")*len(secretword))}") # neat trick here: _ times length of secret word, then " ".join converts them from list to string. this means wtv outputs from len is a list

def initialisation(secretword):
    print(f"Game is starting!")
    while True:
        maxguess = input("Gamemaster, please input the maximum allowable guesses!: ")
        try:
            maxguess = int(maxguess)
            if maxguess <= 0:
                print("Invalid! Maximum guess cannot be zero or lower!")
                continue
            else:
                rightguess = 0
                wrongguess = 0
                guessedletters = set()
                guesscount = 0
                display = ["_"]*len(secretword) # the [] is REALLY important, it shows that we are multiplying len secret word with a list that contains _, instead of just _ which has a NONE Type!!!!
                return maxguess, guesscount, display, guessedletters, rightguess, wrongguess
        except ValueError:
            print("Please input a valid integer!")
            continue

def gamestate(rightguess, wrongguess, guesscount, maxguess, guessedletters):
    print(f"You have guessed {rightguess} correct position(s)!")
    print(f"You have guessesd incorrectly {wrongguess} time(s)!")
    print(f"Your guessed letters are: {guessedletters}")
    print(f"You have {guesscount}/{maxguess} guesses left!")

def getguess(guessedletters, guesscount):
    while True:
        guess = input("Please enter your guess!: ").lower() #.lower() ensures that capitalised and non capitalised letters are good to go!
        if not guess.isalpha():
            print("Please guess a letter!")
            continue
        elif len(guess) != 1: #corrected by deepseek, we are comparing the LENGTH of guess, not guess itself to the number
            print("Please guess 1 character at a time!")
            continue
        elif guess in guessedletters: # corrected by deepseek, we are comparing guess IN guessed letters, not ==
            print("You have already guessed that letter!")
            continue
        else:
            guesscount += 1
            guessedletters.add(guess) # guessedletters + guess does NOT work with sets!
            return guess, guesscount, guessedletters
        
def compareguess(guess, secretword, display, rightguess, wrongguess): #inspired by deepseek, this part is REALLY HARD
    if guess in secretword:   
        for i, letter in enumerate(secretword): # what enumerate does - word = hello | enumerate(word) = [0, h], [1, e], [2, l], [3, l], [4, o] | therefore, i correspond to index, and letter correspond to letter in secretword
            if guess == letter:
                display[i] = guess # this is stupid, if guess == letter, then it will replace all matching indexes (underscores -> letters) who wouldve THUNK
                rightguess += 1
                wrongguess = wrongguess
                result = True
        return rightguess,wrongguess, result # correct guess
    else:
        rightguess = rightguess
        wrongguess += 1
        result = False
        return rightguess, wrongguess, result # wrong guess
    
def main():
    secretword = secretwordprompt()
    #print(f"DEBUG {secretword}")
    #print(f"DEBUG {len(secretword)}")
    #print(f"DEBUG {["_"]*len(secretword)}")
    maxguess, guesscount, display, guessedletters, rightguess, wrongguess = initialisation(secretword)
    displayhidden(secretword) #initial secret word display
    #print(f"DEBUG {display}")
    while "_" in display and guesscount < maxguess:
        gamestate(rightguess, wrongguess, guesscount, maxguess, guessedletters)
        guess, guesscount, guessedletters = getguess(guessedletters, guesscount)
        rightguess, wrongguess, result = compareguess(guess, secretword, display, rightguess, wrongguess)
        if result == True:
            print(f"Congratulation! {guess} was a correct guess!")
            print(f"{display}")
            continue
        else:
            print(f"The guess was not in the word!")
            print(f"{display}")
            continue
    if "_" not in display:
        print(f"Congratulations! you have won the game! The word was {secretword}!!! Thank you for playing!")
    else:
        print(f"You have run out of guesses! Better luck next time! The word was {secretword}!")

if __name__ == "__main__":
    main()