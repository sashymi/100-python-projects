"""
## 11. FizzBuzz
#**Concepts:** For loops, modulo operator (%), conditionals
#**Hints:** Loop 1-100, use modulo to check divisibility by 3 and/or 5, print numbers or words accordingly.

# Integer modulo
print(10 % 3)  # Output: 1 (10 divided by 3 is 3 with a remainder of 1)
print(12 % 4)  # Output: 0 (12 divided by 4 is 3 with a remainder of 0)

# Negative numbers
print(-7 % 3)  # Output: 2 (Python's modulo result takes the sign of the divisor)
print(7 % -3)  # Output: -2

# Floating-point numbers (use with caution due to potential precision issues)
print(3.5 % 0.1)  # Output: 0.09999999999999981 (may not be exactly 0.0 due to float representation)
"""

def main():
    def intro():
        print("Hi and welcome to Sashymi's 100 codes! Today we will make a FizzBuzz program! if divisible by 3, Fizz, if divisible by 5, Buzz, if both, FizzBuzz")

    def userinput():
        while True:
            try:
                maxcount = int(input("Please provide the maximum ceiling value of which FizzBuzz is needed to be calulated: "))
            except ValueError:
                print("You have entered and invalid integer! Please try again!")
            return maxcount

    def logic(maxcount):
        for i in range(1,(maxcount+1)):
            if i % 3 == 0 and i % 5 == 0:
                print(f"For value {i:4}: FizzBuzz")
            elif i%3 != 0 and i % 5 == 0:
                print(f"For value {i:4}: Buzz")
            elif i%3 == 0 and i % 5 != 0:
                print(f"For value {i:4}: Fizz")
            elif i%3 != 0 and i % 5 != 0:
                print(f"For value {i:4}: {i}/3={(i/3):.2f}, {i}/5={(i/5):.2f}")
        return i

    def outtro(i):
        print(f"You have used this FizzBuzz Program for {i} iterations!")

    intro()
    maxcount = userinput()
    logic(maxcount)
    outtro(maxcount)

if __name__ == "__main__":
    main()