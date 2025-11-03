## 10. Multiplication Table
#**Functions needed:** `range()`, `print()`
#**Concepts:** For loops, string formatting
#**Hints:** Use for loop from 1 to 10, multiply input number by loop counter, format output neatly.

def main():

    CodeNo = 10
    project_name= "Multiplication Table"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Core Logic
    def logic():
        while True:
            try:
                userinput = int(input("Please provide me with a number so I may come up with a multiplication table of up to x20!"))
                for i in range(1, 21, 1): #inclusive of 20
                    print(f"{str(i).center(10)}", end="")
                    print(f"{str(userinput*i).center(10)}", end="") # :5, such that i is represented in print within 5 character width, end ="", such that the print does not go to a new line
            except ValueError:
                print("Please provide a valid numerical entry! Thank you!")
                break


    # Output Results
#    def results():
#        print()

    # Outtro
    def outtro():
        print(f"\n\nThank you for playing!")

    # Execution
    intro(CodeNo)
    x = logic()
    #results()
    outtro ()

if __name__ == "__main__":
    main()