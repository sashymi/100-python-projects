## 14. Factorial Calculator
#**Concepts:** For loops or recursion
#**Hints:** Use loop from 1 to n, multiply running total, or use recursive function calling itself.

def main():

    CodeNo = 14
    project_name= "Factorial Calculator"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Core Logic
    def logic():
        while True:
            try:
                # Asks for user input eg. 4!
                userinput = int(input("Please input a number!: "))
                print(f"We will now proceed with the calculations of {userinput}! (which means factorial, it's not me shouting)")
                
                # Special case for zero factorial
                if userinput == 0:
                    result = 1
                    
                elif userinput < 0:
                    result = "Undefined"

                else:
                    # Calculations
                    result=userinput
                    for i in range((userinput-1),0,-1):
                        print(f"Calculating the factorial of {userinput}!, {result} X {i}")
                        result=result*i

            # If error
            except ValueError:
                print("Invalid number! Please try again!")
                continue

            return result    
        
    # Outtro
    def outtro(x):
        print(f"Your answer is {x}. Thank you for playing!")

    # Execution
    intro(CodeNo)
    x = logic()
    outtro (x)

if __name__ == "__main__":
    main()