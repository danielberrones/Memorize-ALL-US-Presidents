from random import randint
from sys import exit

d = {
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

correct = []
wrong = []

print("(To exit, type 'exit')\n")

while True:
    ran = randint(1,46)
    correctAnswer = d[ran]
    userResponse = input(f'U.S. President #{ran}: \n')

    if userResponse == "exit":
        print(f'Total Correct: {len(correct)}, \n{correct}\n')
        print(f'Total Wrong: {len(wrong)}, \n{wrong}')
        exit()
    elif userResponse == correctAnswer:
        tup = (userResponse,ran)
        correct.append(tup)
        print("Correct!\n")
    else:
        tup = (userResponse,ran)
        wrong.append(tup)
        print(d.get((userResponse),"That's wrong.\n"))
        hintOrNo = input("Do you want a hint? (y/n)\n")

        if hintOrNo == 'y':
            print(correctAnswer)
        elif hintOrNo == 'n':
            continue
