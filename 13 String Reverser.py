## 13. String Reverser
#**Concepts:** String slicing
#**Hints:** Use slicing syntax [::-1] to reverse string, or use for loop to build reversed string.

def main():

    CodeNo = 13
    project_name= "String Reverser"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Core Logic
    def logic():
        i = 0
        while True:
            text = input("Please input text which you wish to reverse! (or s to stop!): ")
            if text != "s":
                print(f"Your  text is: {(text)}")        
                print(f"Your reversed text is: {(text)[::-1]}")
                i += 1
                continue
            else:
                print(f"You have played {i} times!")
                break

    # Outtro
    def outtro():
        print(f"Thank you for playing!")

    # Execution
    intro(CodeNo)
    logic()
    outtro ()

if __name__ == "__main__":
    main()