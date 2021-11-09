from random import randint
from sys import exit
from time import sleep

presidents = {
    1: "George Washington",
    2: "John Adams",
    3: "Thomas Jefferson",
    4: "James Madison",
    5: "James Monroe",
    6: "John Quincy Adams",
    7: "Andrew Jackson",
    8: "Martin Van Buren",
    9: "William Henry Harrison",
    10: "John Tyler",
    11: "James K. Polk",
    12: "Zachary Taylor",
    13: "Millard Fillmore",
    14: "Franklin Pierce",
    15: "James Buchanan",
    16: "Abraham Lincoln",
    17: "Andrew Johnson",
    18: "Ulysses S. Grant",
    19: "Rutheford B. Hayes",
    20: "James Garfield",
    21: "Chester Arthur",
    22: "Grover Cleveland",
    23: "Benjamin Harrison",
    24: "Grover Cleveland",
    25: "William McKinley",
    26: "Theodore Roosevelt",
    27: "William Howard Taft",
    28: "Woodrow Wilson",
    29: "Warren Harding",
    30: "Calvin Coolidge",
    31: "Herbert Hoover",
    32: "Franklin D. Roosevelt",
    33: "Harry S. Truman",
    34: "Dwight D. Eisenhower",
    35: "John F. Kennedy",
    36: "Lyndon B. Johnson",
    37: "Richard Nixon",
    38: "Gerald Ford",
    39: "Jimmy Carter",
    40: "Ronald Reagan",
    41: "George H.W. Bush",
    42: "Bill Clinton",
    43: "George W. Bush",
    44: "Barack Obama",
    45: "Donald Trump",
    46: "Joe Biden",
}

v = [v for v in presidents.values()]
def listPres():
    for x in v:
        print(x)

correct = []
wrong = []
hintCounter = 0

def printIntro():
    print("Learn the U.S. Presidents")
    sleep(1)

printIntro()

def showMenu():
    print("Menu")
    print("------------------------")
    print("'score'- show current score")
    print("'pres' - show all presidents")  
    print("'exit' - exit game")
    print("'menu' - show menu")
    print("'clear' - clear screen")
    print("------------------------")
    input("Hit Enter to continue...")

showMenu()

def clearScreen():
    print('\n'*50)

def showStats():
    print(f'Total Hints: {hintCounter}\n')
    print(f'Total Correct: {len(correct)},\n{correct}\n')
    print(f'Total Wrong: {len(wrong)}, \n{wrong}')


while True:
    ranNum = randint(1,46)
    correctAnswer = presidents[ranNum]
    userResponse = input(f'\nU.S. President #{ranNum}: \n')

    if userResponse == "score":
        showStats()
    elif userResponse == "pres":
        listPres()
    elif userResponse == "exit":
        showStats()
        exit()
    elif userResponse == "menu":
        showMenu()
    elif userResponse == "clear":
        clearScreen()
    elif userResponse == correctAnswer:
        tup = (userResponse,ranNum)
        correct.append(tup)
        print("Correct!\n")
    else:
        tup = (userResponse,ranNum)
        wrong.append(tup)
        print(presidents.get((userResponse),"Wrong."))
        
        hintOrNo = input("Need a hint? (y/n)\n")
        if hintOrNo == 'y':
            hintCounter += 1 
            print(correctAnswer)
        elif hintOrNo == 'n':
            continue
