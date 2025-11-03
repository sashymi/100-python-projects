## 16. Simple Alarm Clock
#**Functions needed:** `datetime.datetime.now()`, `time.sleep()`
#**Concepts:** DateTime comparison, while loops
#**Hints:** Get current time, compare with target time in loop, sleep briefly between checks.

from datetime import datetime
import time #has to be imported separately, not from datetime


# process = get current time -> get target time -> compare the two in a loop -> sleep briefly between checks

def main():

    CodeNo = 16
    project_name= "Simple Alarm Clock"

    # Intro
    def intro(CodeNo):
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

    # Functions
    # hh, mm
    def get_alarm():
        while True: #need this for the loop
            target_time = input("Please set your alarm clock in 24-hour format! (hh:mm): ")
            try:
                target_time_hh_str, target_time_mm_str = target_time.split(":") #split the text
#                # check if integer
                target_time_hh = int(target_time_hh_str) #check if hours is integer
                target_time_mm = int(target_time_mm_str) #check if minute is integer
                # check if in range
                if int(0) <= target_time_hh <= int(23) and int(0) <= target_time_mm <= int(59):
                    return str(target_time_hh).zfill(2), str(target_time_mm).zfill(2) #pads return values with zeroes, return will act as a break, will get out of while loop, ZFILL ONLY WORKS WITH STR THO, so we convert back to str before zfill
                else:
                    print("Please input a valid time format (hh:mm)!")
                    continue
            except ValueError:
                print("Please input a valid time format (hh:mm)!")
                continue #if error, continue from 'while True'

    # hh, mm   
    def get_current_time():
        current_time = datetime.now().time()
        return current_time.hour, current_time.minute

    # alarm = 1 or 0
    def comparator(current_time_hh, current_time_mm, target_time_hh, target_time_mm):
        
        # assigning variables
        current_time_hour = current_time_hh
        current_time_min = current_time_mm
        target_time_hour = target_time_hh
        target_time_min = target_time_mm

        # comparator
        while True: ##### please put output in another functioN! then while loop get current time and use recursion for comparator!!!
            alarm = 0
            if int(current_time_hour + current_time_min) == int(target_time_hour + target_time_min): #using and to concatenate is not cool! need to use + to concatenate strings, then convert to integer!
                alarm = 1
                return alarm
            elif int(current_time_hour + current_time_min) < int(target_time_hour + target_time_min): # concatenates hh and mm, already an integer, objective is to compare integer eg. 0040<1230
                print(f"We are waiting for your alarm.. Current time is {current_time_hh}:{current_time_mm}")
                time.sleep(1)
                return alarm
            elif int(current_time_hour + current_time_min) > int(target_time_hour + target_time_min): #edge case, will never be if recursion is correct
                alarm = 2
                return alarm

    def result(alarm, current_time_hh, current_time_mm, target_time_hh, target_time_mm):
        if alarm == 1:
            print(f"It is {current_time_hh}:{current_time_mm}! Alarm has arrived! PLEASE WAKE UP / DO WHAT YOU NEED TO DO!")
        else: print(f"{target_time_hh}:{target_time_mm} happened before {current_time_hh}:{current_time_mm}! Alarm is set past the current time!")

    # Outtro
    def outtro():
        print(f"Thank you for playing!")

    # Logic
    intro(CodeNo)
    target_time_hh, target_time_mm = get_alarm()
    while True:
        current_time_hh, current_time_mm = get_current_time()
        alarm = comparator(current_time_hh, current_time_mm, target_time_hh, target_time_mm)
        if alarm == 0:
            continue
        else:
            break
    result(alarm, current_time_hh, current_time_mm, target_time_hh, target_time_mm)
    outtro ()

if __name__ == "__main__":
    main()