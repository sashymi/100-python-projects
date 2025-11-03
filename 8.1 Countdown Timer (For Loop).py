## 8. Countdown Timer
#**Functions needed:** `time.sleep()`, `print()`
#**Concepts:** For loops, range() with negative step
#**Hints:** Use for loop with range(start, stop, -1), add time.sleep(1) between numbers.

# retake but with for loop instead of while
# range (start, stop, step)
#        for i in range(2, 10, 2):
#            print(i) # Prints 2, 4, 6, 8

import time

def main():

    # Intro
    def intro():
        print("Hi and welcome to Sashymi's 100 codes! You are at Code No 8! This time we'll play with a countdown timer 2.0! It's the exact same time but with a for loop!")

    # User Input
    def user_input(): #Finding maxvalue
        while True: #important for True to have capitalised T
            try:
                x = int(input("Please enter your countdown value: "))
                return x
            except ValueError:
                print("Invalid number! Please try again")

    # Process
    def processing(maxvalue):
        for i in range(maxvalue, 0, -1): # (start, stop, step), so start at max, then reduce down to zero
            print(f"Currently counting down from {i}!")
            time.sleep(1)
#            i-=1 #this does NOTHING, because for loop already has incremental reductions defined above

    # Outtro
    def outtro(maxsecond):
        print(f"You have counted down from {maxsecond}! Thank you for playing!")

    # Function call
    intro()
    x = user_input()
    processing (x)
    outtro (x)

if __name__ == "__main__":
    main()