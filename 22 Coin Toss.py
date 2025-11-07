## 22. Coin Toss Simulation
#**Functions needed:** `random.choice()`
#**Concepts:** For loops, counters
#**Hints:** Use list ['heads','tails'], loop 1000 times, increment counters for each result.

# Plan
# 1. Ready to start coin tossing? (Y/N)
# 2. Random toss x1000
# 3. Results display percentage of tosses

import random

def initialisation():
    heads_or_tails = ["heads", "tails"]
    heads = 0
    tails = 0
    while True:
        ready = input("Ready to start coin tossing? (y/n): ")
        if ready == "y":
            return heads_or_tails, heads, tails
        else:
            print("You have to be ready to play :p")
            continue

def toss_counter():
    toss_count = 0
    while True:
        try:
            max_toss_count = int(input("Please enter how many coin tosses you wish to perform: "))
            return toss_count, max_toss_count
        except ValueError:
            print("Please enter a valid number!")
            continue
    

def cointoss(toss_count, heads_or_tails, heads, tails):
    toss_result = random.choice(heads_or_tails)
    toss_count += 1
    if toss_result == "heads":
        heads += 1
        return toss_result, heads,tails, toss_count
    else:
        tails += 1
        return toss_result, heads, tails, toss_count
    
def main():
    heads_or_tails, heads, tails = initialisation()
    toss_count, max_toss_count = toss_counter()
    smallmultiplier = max_toss_count // 10
    while toss_count < max_toss_count:
        toss_result, heads, tails, toss_count = cointoss(toss_count, heads_or_tails, heads, tails)
        if toss_count%smallmultiplier == 0:
            print(f"Coin toss no. {toss_count}, {toss_count/max_toss_count*100:.2f}% of the way there!\nYour toss result is {toss_result},\nHeads Count: {heads/max_toss_count*100:.2f}%\nTails Count: {tails/max_toss_count*100:.2f}%")
    print(f"A {toss_count} coin tosses have been executed.\nThe results are:\nHeads: {heads/max_toss_count*100:.2f}%\nTails: {tails/max_toss_count*100:.2f}%")
    if heads > tails:
        print("Verdict: Heads!")
    elif tails > heads:
        print("Verdict: Tails!")
    else:
        print("It's a tie!")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()