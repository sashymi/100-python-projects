## 15. Temperature Converter
#**Concepts:** Arithmetic formulas
#**Hints:** F to C: (F-32)*5/9, C to F: (C*9/5)+32. Ask user which conversion they want.

def main():

    CodeNo = 15
    project_name= "Temperature Converter"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Functions
    def get_converter():
        while True: #if expecting string inputs, no need try and except, that is only for int or float checks! the more you know
            
            userinput = input("Which converter would you like to use?\nType 'f' for celcius to fahrenheit\nType 'c' for fahrenheit to celcius: ")

            if userinput == "f":
                return "f"
            elif userinput == "c":
                return "c"
            else:
                print("Please enter a valid input!")

            # while true will exit loop only if input is either f or c, because of the return function

    def get_temperature():
        try:
            userinput = float(input("What is your temperature value?: "))
            return userinput
        except ValueError:
            print("Please enter a valid input!")

    def fahrenheit_converter(temperature):
        fahrenheit = (temperature*9/5)+32
        return fahrenheit
    
    def celcius_converter(temperature):
        celcius = (temperature-32)*5/9
        return celcius
    
    # Core Logic - this program uses recursion
    def logic():
        converter = get_converter()
        temperature = get_temperature()
        if converter == "f":
            result = fahrenheit_converter(temperature)
            print(f"You have used a fahrenheit converter for a value of {temperature} deg C --> {result} deg F!")
        elif converter == "c":
            result = celcius_converter(temperature)
            print(f"You have used a celcius converter for a value of {temperature} deg F --> {result} deg C!")

    # Outtro
    def outtro():
        print(f"Thank you for playing!")

    # Execution
    intro(CodeNo)
    logic()
    outtro()

if __name__ == "__main__":
    main()

# What I have learned
# This is the first time I am coding with with recursion & functions use
# a concept deepseek broght up was 'Single Responsibility Principle', where each function only has one specific thing that it does
# 1 thing is its really straightforward, but 2nd thing is its quite complex, especially when we are thinking about tuples, how to return values, how to recall the values in other functions etc