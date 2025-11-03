## 12. Odd or Even
#**Concepts:** Modulo operator (%)
#**Hints:** Use number % 2 == 0 to check if even, else it's odd.

def main():

    CodeNo = 12
    project_name= "Odd & Even Checker"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Core Logic
    def logic():
        while True:
            # User input
            userinput = input("Please input a number for us to check if it is Odd or Even! (s to stop): ")
            # Odd Even Check
            if userinput == "s":
                print("Thank you for playing!")
                break
            elif userinput != "s":
                try:
                    result = int(userinput)%2
                    if result == 0:
                        print(f"Your number {userinput} is even!")
                    else: print(f"Your number {userinput} is odd!")
                except ValueError:
                    print (f"Your input is invalid! Please try again!")

    # Execution
    intro(CodeNo)
    logic()

if __name__ == "__main__":
    main()