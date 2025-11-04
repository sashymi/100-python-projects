## 19. Palindrome Checker
#**Concepts:** String methods (lower(), replace()), string reversal
#**Hints:** Clean string (remove spaces, lowercase), compare with reversed version using slicing.

# plan for code
# input > check for odd or even (does not matter), check for no of characters > //2 > compare each front chara to each back chara > if all is equal, palindrome > else not palindrome

def intro():
        CodeNo = 19
        project_name = "Palindrome Checker"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

# Global Variables / Constants

# Helper Documentation
def readme():
       """
       Palindrome checker! Plan for code is as follows
       - get input from user
       - check no of characters for input and //2
       - compare each front chara with back chara
       - if same palindrome, else not palindrome
       """

# Core Logic Functions
def userinput():
    wordtocheck = input("Please enter a word to check if it is a palindrome!: ")
    return wordtocheck

def characterchecker(wordtocheck):
    while True:
        if len(wordtocheck)%2 == 0: # even length, therefore no need to remove middle index before splitting
            checkedword = len(wordtocheck) //2
            firsthalf = wordtocheck[:checkedword]
            secondhalf = wordtocheck[checkedword:]
#            print(f"DEBUG {firsthalf}, {secondhalf}")
            return firsthalf, secondhalf
        else:
            checkedword = len(wordtocheck) //2# for odd words, we remove middle index first
            firsthalf = wordtocheck[:checkedword]
            secondhalf = wordtocheck[checkedword+1 :]# secondhalf is different, since we remove the middle index first before splitting
#            print(f"DEBUG {firsthalf}, {secondhalf}")
            return firsthalf, secondhalf

def comparator(firsthalf, secondhalf):
    secondhalf = f"{secondhalf}"[::-1]
#    print(f"DEBUG {firsthalf}, {secondhalf}")
    if firsthalf == secondhalf:
        palindrome = 1
    else:
        palindrome =0

    return palindrome

# Main Implementation / Result
def main():
    intro()
    while True:
        wordtocheck = userinput()
        firsthalf, secondhalf = characterchecker(wordtocheck)
        result = comparator(firsthalf, secondhalf)
        if result == 1:
            print(f"Your word {wordtocheck} is a palindrome!")
        else:
            print(f"Your word {wordtocheck} is NOT a palindrome!")

        nextstep = input("Do you wish to play again? (y/n): ")
        if nextstep == "y":
            continue
        else:
            break
    outtro()
         
if __name__ == "__main__":
    main()