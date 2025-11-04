## 18. Find the Largest Number
#**Concepts:** Lists, for loops, comparison
#**Hints:** Assume first number is largest, loop through rest comparing each number to current largest.

def intro():
        CodeNo = 18
        project_name = "Find the Largest Number"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

# Global Variables / Constants

# Helper Documentation
def readme():
       """
       
       """

# Core Logic Functions

# User input
# number

def getnum():
    while True:
        try:
            number = int(input("Please enter a number you wish to compare: "))
            return number
        except ValueError:
            continue
            

def comparenum(number, storednum):
    #largestnum
        #comparator
    if storednum == number:
        print(f"Your {number} when compared with {storednum}, is the same!")
        return number
    elif storednum < number:
        print(f"Your {number} when compared to {storednum}, {number} is bigger!")
        return number
    elif storednum > number:
        print(f"Your {number} when compared to {storednum}, {storednum} is bigger!")
        return storednum

def output(largestnum):
    print(f"Your current largest number is {largestnum}!")

# Main Implementation / Result
def main():
    storednum = 0
    while True:
        number = getnum()
        largestnum = comparenum(number, storednum)
        storednum = number
        repeat = input("Do you wish to enter another number? (Y/N): ")
        if repeat == "Y":
            output(largestnum)
            continue
        elif repeat == "N":
            break
        else:
            print("Please input a valid response!")

    output(largestnum)
    outtro()

if __name__ == "__main__":
    main()