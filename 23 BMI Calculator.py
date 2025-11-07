## 23. BMI Calculator
#**Concepts:** Arithmetic, comparison
#**Hints:** BMI = weight(kg) / height(m)². Add categories (underweight, normal, overweight) based on BMI ranges.

# Planning
# 1. getdata - weight and height
# 2. getbmi
# 3. printresults

def intro():
        CodeNo = 23
        project_name = "BMI Calculator"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

def getdata():
    while True:
        try:
            weight = float(input("Please enter your weight (kg): "))
            height = float(input("Please enter your height (cm): "))
            
            if weight > 635:
                print("You can't possibly be heavier than the heaviest human ever recorded in human history...")
                continue
            elif height > 272:
                print("You can't possibly be taller than the tallest human ever recorded in human history...")
                continue
            elif weight < 2 or height < 54:
                print("That can't be right...")
            else:
                return weight, height
        except ValueError:
            continue

def getbmi(weight, height):
    height_m = height / 100
    bmi = weight / ((height_m)**2) # ** means to the power of
    return float(bmi)

def bmiclass(bmi):
    if bmi < 18.5:
        return "under-weight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "over-weight"
    elif bmi < 35:
        return "obese class 1"
    elif bmi < 40:
        return "obese class 2"
    else:
        return "obese class 3"

# Main Implementation / Result
def main():
    intro()
    weight, height = getdata()
    bmi = getbmi(weight, height)
    category = bmiclass(bmi)
    print(f"Your weight is {weight:.2f}kg, your height is {height:.2f}cm\nYour BMI is calculated to be {bmi:.2f}\nYou are {category}!")
    outtro()

if __name__ == "__main__":
    main()
        
