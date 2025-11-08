## 24. Leap Year Checker
#**Concepts:** Modulo operator, conditional logic
#**Hints:** Divisible by 4 AND (not divisible by 100 OR divisible by 400).

# 1000 BC -> 1 BC -> 1 AD -> 2025 AD
# 1. define BC or AD, enter year, cannot be zero
# 2. convert BC to -ve
# 3. comparator
# 4. 

"""if year < 1582:
    # Julian calendar rules (before Gregorian reform)
    if year % 4 == 0:
        leap year = true
    else:
        leap year = false
else:
    # Gregorian calendar rules (from 1582 onward)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap year = true
    else:
        leap year = false"""

def intro():
        CodeNo = 24
        project_name = "Leap Year Checker"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

def entryyear():
    while True:
        try:
            yeartocheck = int(input("Please enter the year you wish to check for leap year: "))
            AD_BC = input("Please define if your calendar year is in AD or BC (ad/bc): ")
            if AD_BC == "ad" or AD_BC == "bc": #.lower will make it so wtv input by user, will always be formatted as lowercase
                return yeartocheck, AD_BC
            else:
                print("Please input a valid entry (ad/bc)")
                continue
        except ValueError:
            print("Please input a valid year!")
            continue

def formatyear(AD_BC, yeartocheck):
    formattedyear = f"{yeartocheck} {AD_BC.upper()}"
    return formattedyear

def bcconversion(AD_BC, yeartocheck):
    if AD_BC == "bc":
        yeartocheck = -yeartocheck -1
        #print(f"DEBUG - Year to check is run through BC conversion: {yeartocheck}")
        return yeartocheck
    else:
        #print(f"DEBUG - Year to check is NOT run through BC conversion: {yeartocheck}")
        return yeartocheck

# Main Implementation / Result

def main():

    intro()
    checkcount = 0
    while checkcount == 0:
        yeartocheck, AD_BC = entryyear()
        formattedyear = formatyear(AD_BC, yeartocheck)
        yeartocheck = bcconversion(AD_BC, yeartocheck)
        if yeartocheck < 1582:
            if yeartocheck % 4 == 0:
                print(f"{formattedyear} is a leap year!")
            else:
                print(f"{formattedyear} is NOT a leap year!")
        else:
            if (yeartocheck % 4 == 0 and yeartocheck % 100 != 0) or yeartocheck % 400 == 0:
                print(f"{formattedyear} is a leap year!")
            else:
                print(f"{formattedyear} is NOT a leap year!")
        checkcount += 1

        while checkcount == 1:
            nextstep = input("Would you like to check for another year? (y/n)?: ")
            if nextstep == "y".lower():
                checkcount = 0
                break
            elif nextstep == "n".lower():
                break
            else:
                print("Please enter a valid response!")
                continue
    outtro()

if __name__ == "__main__":
    main()