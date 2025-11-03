## 17. Basic To-Do List
#**Concepts:** Lists, list methods (append, remove)
#**Hints:** Use empty list to store tasks, provide menu options (add, view, remove), modify list based on user choice.

#tasks = []  # Create empty list

# These methods are available immediately:
#tasks.append("Buy groceries")    # Add to end
#tasks.remove("Buy groceries")    # Remove by exact value
#tasks.pop(0)                     # Remove by index position

#tasks.insert(0, "Urgent task")  # Insert at specific position
#tasks.clear()                   # Remove all tasks
#tasks.count("task")             # Count occurrences
#tasks.index("task")             # Find position of task

def intro():
        CodeNo = 17
        project_name = "Basic To-do List"
        print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
        print(f"Thank you for playing!")

# Global Variables / Constants
mylist = []

# Helper Documentation
def readme():
       """
       
       """

# Core Logic Functions - 1. add task, 2. remove task, 3. edit task??? maybe too hard?
def addtask():
    addtask = input("Please input a task: ")
    if len(mylist) > 0:
        taskno = 0
        taskno = len(mylist) + 1 #have to do it this way, cannot +=, not sure why??? maybe because its not an integer? but it is tho
        taskno = f"{taskno}. {addtask}"#str(taskno) + ". " #dumb way to do this.
        mylist.append(taskno) # task is added to list, ##task no is a set, a new parameter that i discovered!! who knew!
    else:
        mylist.append("1. " + addtask) # task is added to list
    print ("Your task has been added!")
    print(mylist)

def removetask():
    print(len(mylist))
    if len(mylist) > 0:
        while True:
            try:
                print(mylist)
                removetask = int(input("Please select which task number you wish to remove: "))
                break #goes down
            except ValueError:
                print("Please enter a valid input!")
                nextstep = input("Do you still wish to remove a task? (Y/N): ")
                if nextstep == "Y":
                    continue #goes to after while
                else:
                    return None #goes out of the function
    else:
        print("Your list is empty!")
        return None
    print(f"You have decided to remove task no. {removetask}!")
    mylist.pop(int(removetask-1))
    print(mylist)
    print(f"Task no. {removetask} has been successfully removed!")

# Main Implementation - landing page here
def main():
    intro()
    while True:
        userinput = input("What would you like to do? (Please enter a number)\n1. Add a task\n2. Remove a task\n3. Show current to do list\n4. Exit the program\n") #string, even though the user inputs a number
        if userinput == "1":
            addtask()
            continue
        elif userinput == "2":
            removetask()
            continue
        elif userinput == "3":
            print(mylist)
            continue
        elif userinput == "4":
            break
        else:
            print("Please provide a correct prompt!")
            continue #goes to after while true
    outtro()
if __name__ == "__main__":
    main()