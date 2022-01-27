from random import shuffle
from sys import exit
from time import sleep

class Game:
    def __init__(self):
        self.hintCounter = 0
        self.correct = []
        self.wrong = []
        self.presidents = {
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
            46: "Joe Biden"
            }   

    def exitGame(self):
        exit()

    def listPres(self):
        v = [v for v in self.presidents.items()]
        print(v)
        sleep(5)

    def printIntro(self):
        print("\nLearn the U.S. Presidents!")
        sleep(1.5)

    def showMenu(self):
        print("\n[Menu]")
        sleep(.5)
        print("'exit' - exit game")
        sleep(.5)
        print("'menu' - show menu")
        sleep(.5)
        print("'pres' - show all presidents")  
        sleep(.5)
        print("'stats'- show stats")
        sleep(2)
        input("\nHit enter to continue game...")

    def showStats(self):
        print("\n\n\n\n[Stats]")
        print(f'Total Hints: {self.hintCounter}\n')
        print(f'Total Correct: {len(self.correct)},\n{self.correct}\n')
        print(f'Total Wrong: {len(self.wrong)}, \n{self.wrong}')
        sleep(3)


def main():
    game = Game()
    game.printIntro()
    game.showMenu()
    presRange = [i for i in range(1,47)]
    shuffle(presRange)
    for i in presRange:
        correctAnswer = game.presidents[i]
        userResponse = input(f'\n\n\n\nU.S. President #{i}: \n')
        if userResponse == "stats":
            game.showStats()
        elif userResponse == "pres":
            game.listPres()
        elif userResponse == "exit":
            game.showStats()
            game.exitGame()
        elif userResponse == "menu":
            game.showMenu()
        elif userResponse == correctAnswer:
            tup = (userResponse,i)
            game.correct.append(tup)
            print("Correct!\n")
        else:
            tup = (userResponse,i)
            game.wrong.append(tup)
            print(game.presidents.get((userResponse),"Wrong."))
            sleep(1)
            hintOrNo = input("Want a hint? (y/n)\n")
            if hintOrNo == 'y':
                game.hintCounter += 1 
                print(correctAnswer)
                sleep(2)
            elif hintOrNo == 'n':
                continue
    game.showStats()
    game.exitGame()


main()
