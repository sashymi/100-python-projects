""""""
## 21. Hangman Game
#**Concepts:** While loops, strings, lists, conditionals
#**Hints:** Track guessed letters, display word with blanks, count wrong guesses, end after 6 wrong or word complete.

#input by gamemaster - word > randomise removal with random.sample, removal length  > while loop 6 iterated guesses > compare with original word using string.index

"""my_string = "hello world"
character_to_find = "o"

try:
    index = my_string.index(character_to_find)
    print(f"'{character_to_find}' found at index {index}.")
except ValueError:
    print(f"'{character_to_find}' not found in the string.")"""

"""    original_list = [1, 2, 3, 4, 5, 6, 7]
    num_replacements = 3
    replacement_value = 'X'

    indices_to_replace = random.sample(range(len(original_list)), num_replacements)"""

def intro():
        CodeNo = 21
        project_name = "Hangman Game"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

# Hangman word by gamemaster
def gamemaster():
    secretword = input("Gamemaster: Please input a word for the Hangman Game!: ")
    return secretword

# Hangman processor to remove random indices from the word
"""
def hangmanprocessor(hangmanword, removedwords):
    hangmanwordlist = list(hangmanword) # converts hangmanword to list
    charareplacement = len(hangmanwordlist)//2 # looks for the length of hangmanword and divide 2 rounded down
    charareplacewith = "_" # what character to replace the removed characters wtih
    removedwords = random.sample(range(len(hangmanwordlist)), charareplacement) # remove characters here!
    for index in removedwords:
          hangmanwordlist[index] = charareplacewith # replace removed characters with variable charareplacewith
    hangmanwordlist = " ".join(hangmanwordlist) # converts from list to string
"""

def showword(secretword):
    print(f"The length of your word is {len(secretword)} letters.")

    # initial display with all underscores
    display = " ".join(["_"]*len(secretword)) # _ times length of secret word, then " ".join converts them from list to string. this means wtv outputs from len is a list
    print(f"Your word is {display}")
    """hangmanwordlist = list(secretword) # converts hangmanword to list
    hangmanwordlist = " ".join(hangmanwordlist) # converts from list to string, also inserts space between letters for better readability
    maskedhangmanwordlist = 
    print(f"Your word is {hangmanwordlist}")"""
    return display #secretword is returns in gamemaster function
""""""