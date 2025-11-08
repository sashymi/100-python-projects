## 25. Simple Quiz
#**Concepts:** Lists/dictionaries for questions, score tracking
#**Hints:** Store questions and options in data structure, loop through them, compare user option with correct option, increment score.

# mcq with dictionaries
# 1 user inputs questions and option
# 2 does it have more options? / ready for next question? / start game
# 3 yes, repeat, no move on, repeat question prompt
# 4 if start game, then prompt q and options one by one
# 5 if option == q, score + 1, then move on to next question, else move on to next q
# 6 


def intro():
    CodeNo = 25
    project_name = "Simple Quiz"
    print(f"Hi and welcome to Sashymi's 100 codes! You are at Code No {CodeNo}! Our program for today is {project_name}!")

def outtro():
    print(f"Thank you for playing!")

def initialisation():
    questionno = 0
    mydict = [] # has to be a list [], cannot be dictionaries in dictionaries, but dictionaries in list
    smoldict = {}
    correctcounter = 0
    quizcounter = 0
    return questionno, mydict, correctcounter, quizcounter, smoldict

def userinput(questionno):
    questionno += 1
    question = input(f"Question No {questionno}: ")
    option1 = input(f"Option 1 for Question No {questionno}: ")
    option2 = input(f"option 2 for Question No {questionno}: ")
    option3 = input(f"option 3 for Question No {questionno}: ")
    option4 = input(f"option 4 for Question No {questionno}: ")

    while True:
        try:
            answer = int(input(f"Answer for Question No {questionno} (1/2/3/4): "))
            if answer < 1 or answer > 4:
                print("Please enter a valid option number! (1/2/3/4)")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid option number!")
            continue
    
    return questionno, question, [option1, option2, option3, option4], answer

def answerprompt(questionno):
    while True:
        try:
            answer = int(input(f"Answer for Question No {questionno} (1/2/3/4): "))
            if answer < 1 or answer > 4:
                print("Please enter a valid option number! (1/2/3/4)")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid option number!")
            continue
    return answer

def storetodict(mydict, question, options, answer, smoldict):
    # Neat trick here, using a smaller dictionaries to store the gamemaster inputs, then append it to the big dictionary! only the option/options s usage is making me dumber the more i think about it | corrected by deepseek
    smoldict={
        "question": question,
        "options": options,
        "answer": answer
        }
    mydict.append(smoldict)
    return mydict

def displayquestion(mydict, questionno):
    q = mydict[questionno] # question number, because mydict is a list, not a dictionary, so this new line is introduced | gpt
    print(f"Question {questionno}: {(q["question"])}")
    for i, option in enumerate(q["options"], 1): # this is updated by | gpt
        print(f"{i}.{option}")

def main():
    intro()
    questionno, mydict, correctcounter, quizcounter, smoldict = initialisation()
    print("----------Gamemaster----------")
    step = 0
    while step == 0:
        questionno, question, options, answer = userinput(questionno)
        mydict = storetodict(mydict, question, options, answer, smoldict)
        while True:
            try:
                nextstep = int(input(f"Question No {questionno} is done!\n1. Enter another question\n2. Proceed to Quiz"))
                if nextstep == 1:
                    step = 0
                    break
                elif nextstep == 2:
                    step = 1
                    break
                else:
                    print("Please enter a valid option number!")
                    continue
            except ValueError:
                print("Please enter a valid option number!")
                continue
    print("----------Player----------")
    questioncounter = questionno-1
    while quizcounter <= questioncounter:
        displayquestion(mydict, quizcounter) # use quizcounter as index | gpt
        playeranswer = answerprompt(quizcounter + 1) # |gpt
        q = mydict[quizcounter] #|gpt
        quizcounter += 1
        # getting the values of index instead of comparing integer to integer | corrected by deepseek
        correctoptiontext = q["options"][q["answer"]-1] # | gpt
        playeroptiontext = q["options"][playeranswer - 1]
#        if playeranswer == mydict["answer"]: cannot use! | corrected by deepseek
        if correctoptiontext == playeroptiontext:
            print("Correct! ✅")
            correctcounter += 1
        else: 
            print(f"Incorrect! ❌. Correct answer was {q["answer"]}")

    print(f"You have answered a total of {questionno} question!\nYou got {correctcounter}/{questionno} questions correct! See you next time!")

    outtro()

if __name__ == "__main__":
    main()