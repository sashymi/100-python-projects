## 8. Countdown Timer
#**Functions needed:** `time.sleep()`, `print()`
#**Concepts:** For loops, range() with negative step
#**Hints:** Use for loop with range(start, stop, -1), add time.sleep(1) between numbers.

# first try on time! excited
# we'll make this abit more interesting, lets make each second print to terminal, so the user will be able to see the countdown happening in real time
# we'll also play with seconds only on this one :P

import time

# Main program starts
def main():

    # Introduction
    def intro():
        print("Hi and welcome to Sashymi's 100 codes! You are at Code No 8! This time we'll play with a countdown timer!")

    # User input
    def userinput():
        while True: # Keep asking until a valid input is achieved
            try:
                maxsecond = int(input("Please set how many seconds you wish to count down from: "))
                return maxsecond # this will return the maxsecond 
            except ValueError:
                print("You entered a non-integer! Please try again!")
        
    # Program
    def countdown(maxsecond):
        currentsecond = 0
        countdownsecond = maxsecond
        print("Program is now starting! Please wait a moment...")
        while currentsecond < maxsecond: # < instead of <= to avoid counting an extra second the moment enter is hit
            print(f"Counting down from {countdownsecond}seconds ...")
            time.sleep (1) # Pause for 1 second
            currentsecond += 1
            countdownsecond -= 1

    # Outtro
    def outtro(maxsecond):
        print(f"You have counted down from {maxsecond}! Thank you for playing!")

    intro()
    second = userinput()
    countdown(second)
    outtro(second)

if __name__ == "__main__":
    main()

# while true is more useful than you think, esp for user input, when combined with try and except, it will repeat the input prompt until it is true
# local variables in each separate functions are unique, if you return the variable, it will then store the value as the function itself. for example, maxseconds is destroyed and userinput() itself becomes wtv maxsecond was
# this means that you dont have to name maxseconds all the way down in the other functions, they can be named whatever, and userinput() can be assigned to a global variable, and that variable can be called in the other functions!
