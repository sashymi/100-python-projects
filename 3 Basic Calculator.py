# 3. Basic Calculator
# **Functions needed:** `input()`, `print()`, `float()`
# **Concepts:** Variables, arithmetic operators (+, -, *, /), if/elif/else
# **Hints:** Convert inputs to numbers, ask for operation type, use conditionals for different math operations.

first_number = input("What is your first number?")

try: first_number = float(first_number)
except ValueError:
    print("Number is invalid!")        #indentations are important!! if this is indented to the left, it will not be in except function
    exit()                             #if this is indented to the left, it will exit the whole program altogether!!

second_number = input("What is your second number?")

try: second_number = float(second_number)
except ValueError:
    print("Number is invalid!")        #indentations are important!! if this is indented to the left, it will not be in except function
    exit()                             #if this is indented to the left, it will exit the whole program altogether!!

operator = input("Which operator would you like to use? (+, -, *, /)")

if operator=="+": print(float(first_number) + float(second_number))
elif operator=="-": print(float(first_number) - float(second_number))
elif operator=="*": print(float(first_number) * float(second_number))
elif operator=="/": print(float(first_number) / float(second_number))
else: print("Invalid operator!")

print ("Thank you for using Sashymi's Calculator! Have a nice day!")

# What have I learned?
# 1. float to be used only when you want to print it as a number. for example, if you want to store a float into a variable, you dont need float function. only when you wish to print it or perform maths on it
# 2. difference between = and ==, = is one directional, for example - a variable getting assigned a value. == is birectional, its for operations. so always use == if comparing between two things / values / variables
# 3. if, elif, elif, elif, else. the 'then' is identified as :
# 4. always have fallbacks, if invalid operator, if invalid number etc. in this case, an invalid operator check is there, but not an invalid number check
# 5. invalid number check is done at line 8 and line 15! we use try and except. for example try the first number and use it as a float, if the value is error, therefore it is an invalid number! 
# and this is remarked as ValueError which i think is a universal variable
# 6. another thing that is worth noting is, once the number is stored as a float in the try and except, there is no need to call the float function again in the operator functions. which means
# if operator=="+": print(first_number + second_number) should work! because the variables first_number and second_number are already stored as float in the try and except function above!
# 7. a final edge case that is not handled in this calculator is division by zero, which is already handled by vscode :p