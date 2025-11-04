## 20. Simple Password Generator
#**Functions needed:** `random.choice()`, `string` module
#**Concepts:** Lists, string concatenation
#**Hints:** Use string.ascii_letters + string.digits + string.punctuation, use random.choice() in loop.

# planner - multiple inputs: small chara, big chara, digits, punctuations > split ascii letter to small and big > core generator > result

import random
import string

def intro():
        CodeNo = 20
        project_name = "Simple Password Generator"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

# Global Variables / Constants

# Helper Documentation
def readme():
       """
       simple password generator
       1. ask for 4 types of inputs, else invalid
       2. split ascii to smol and big - not needed because string.ascii_lowercase exists
       3. core logic
       4. result
       """

# Core Logic Functions
def userinput():
    
    while True:

        smolchara = input("Would you like to generate password with small characters? (y/n): ")
        bigchara = input("Would you like to generate password with big characters? (y/n): ")
        digits = input("Would you like to generate password with digits? (y/n): ")
        punctuations = input("Would you like to generate password with punctuations? (y/n): ")

        if smolchara == "n" and bigchara == "n" and digits == "n" and punctuations == "n":
            print("Your password cannot contain nothing!")
            continue
        elif smolchara == "n" and bigchara == "n" and digits == "n" and punctuations == "y":
            return "0001"
        elif smolchara == "n" and bigchara == "n" and digits == "y" and punctuations == "n":
            return "0010"
        elif smolchara == "n" and bigchara == "n" and digits == "y" and punctuations == "y":
            return "0011"
        elif smolchara == "n" and bigchara == "y" and digits == "n" and punctuations == "n":
            return "0100"
        elif smolchara == "n" and bigchara == "y" and digits == "n" and punctuations == "y":
            return "0101"
        elif smolchara == "n" and bigchara == "y" and digits == "y" and punctuations == "n":
            return "0110"
        elif smolchara == "n" and bigchara == "y" and digits == "y" and punctuations == "y":
            return "0111"
        elif smolchara == "y" and bigchara == "n" and digits == "n" and punctuations == "n":
            return "1000"
        elif smolchara == "y" and bigchara == "n" and digits == "n" and punctuations == "y":
            return "1001"
        elif smolchara == "y" and bigchara == "n" and digits == "y" and punctuations == "n":
            return "1010"
        elif smolchara == "y" and bigchara == "n" and digits == "y" and punctuations == "y":
            return "1011"
        elif smolchara == "y" and bigchara == "y" and digits == "n" and punctuations == "n":
            return "1100"
        elif smolchara == "y" and bigchara == "y" and digits == "n" and punctuations == "y":
            return "1101"
        elif smolchara == "y" and bigchara == "y" and digits == "y" and punctuations == "n":
            return "1110"
        elif smolchara == "y" and bigchara == "y" and digits == "y" and punctuations == "y":
            return "1111"
        else:
            print("Please only use either (y/n)!")
            continue

def logic(pwtype):
    if pwtype == "1111":
        chara = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        return chara
    elif pwtype == "0001":
        chara = string.punctuation
        return chara
    elif pwtype == "0010":
        chara = string.digits
        return chara
    elif pwtype == "0011":
        chara = string.digits + string.punctuation
        return chara
    elif pwtype == "0100":
        chara = string.ascii_uppercase
        return chara
    elif pwtype == "0101":
        chara = string.ascii_uppercase + string.punctuation
        return chara
    elif pwtype == "0110":
        chara = string.ascii_uppercase + string.digits
        return chara
    elif pwtype == "0111":
        chara = string.ascii_uppercase + string.digits + string.punctuation
        return chara
    elif pwtype == "1000":
        chara = string.ascii_lowercase
        return chara
    elif pwtype == "1001":
        chara = string.ascii_lowercase + string.punctuation
        return chara
    elif pwtype == "1010":
        chara = string.ascii_lowercase + string.digits
        return chara
    elif pwtype == "1011":
        chara = string.ascii_lowercase + string.digits + string.punctuation
        return chara
    elif pwtype == "1100":
        chara = string.ascii_lowercase + string.ascii_uppercase
        return chara
    elif pwtype == "1101":
        chara = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        return chara
    elif pwtype == "1110":
        chara = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return chara
    
def pwL():
    while True:
        try:
            pwlength = int(input("Please enter the desired length of your password: "))
            return pwlength
        except ValueError:
            print("Please enter a valid integer!")
            continue

def password(chara, pwlength):
    pwsetup = random.choices(chara, k=pwlength)
    pw = f"".join(pwsetup)
    print(f"Your password is: {pw}")
    return pw

# Main Implementation / Result
def main():
    intro()
    i = 2
    while i == 2:
        pwtype = userinput()
        pwlength = pwL()
        i = 1
        while i == 1:
            chara = logic(pwtype)
            pw = password(chara, pwlength)
            while True:
                nextstep = input(f"What would you like to do?\nEnter 1 to regenerate password\nEnter 2 to redefine password requirements\nEnter 3 to exit\nCurrent generated password is {pw}")
                if nextstep == "1":
                    i = 1
                    break
                elif nextstep == "2":
                    i = 2
                    break
                elif nextstep == "3":
                    outtro()
                    exit()
                else:
                    print("Please input a valid response!")
                    continue
    outtro()

if __name__ == "__main__":
    main()