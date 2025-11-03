## 9. Sum of Numbers
#**Functions needed:** `input()`
#**Concepts:** While loops, break statement, type conversion
#**Hints:** Use while True loop, break when user types "stop", convert inputs to numbers and accumulate sum.

def main():

    CodeNo = 9
    project_name= "Sum of Numbers, where we will add numbers up until the user tells us to stop"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Core Logic
    def logic():

        userinput = input("Please input a number to add or (s to stop): ")
        total = userinput # Initialisation
        print(f"Your current value is {total}!")

        while True:
            userinput = input("Please input a number to add or (s to stop): ")
            if userinput == "s":
                print("Thank you for your time!")
                break
            else:
                try:
                    userinput = int(total) + int(userinput)
                    total = userinput
                    print(f"Your current value is {total}!")
                    
                except ValueError:
                    print("Please input a valid integer!")

        return total
                
    # Output Results
    def results(x):
        print(f"You have added up to the value of {x}!")

    # Outtro
    def outtro():
        print(f"Thank you for playing!")

    # Execution
    intro(CodeNo)
    x = logic()
    results(x)
    outtro ()

if __name__ == "__main__":
    main()

# What I have learned
# simple repeat is as follows, no BS code
# prompt for input > while true > if edge case, then break > else, then do program (if program require input of a number, then try except) > return value to function > end
