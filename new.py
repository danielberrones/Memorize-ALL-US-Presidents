import tkinter as tk
import random

# List of U.S. Presidents
presidents = [
    ("George Washington", 1789),
    ("John Adams", 1797),
    ("Thomas Jefferson", 1801),
    ("James Madison", 1809),
    ("James Monroe", 1817),
    ("John Quincy Adams", 1825),
    ("Andrew Jackson", 1829),
    ("Martin Van Buren", 1837),
    ("William Henry Harrison", 1841),
    ("John Tyler", 1841),
    ("James K. Polk", 1845),
    ("Zachary Taylor", 1849),
    ("Millard Fillmore", 1850),
    ("Franklin Pierce", 1853),
    ("James Buchanan", 1857),
    ("Abraham Lincoln", 1861),
    ("Andrew Johnson", 1865),
    ("Ulysses S. Grant", 1869),
    ("Rutherford B. Hayes", 1877),
    ("James A. Garfield", 1881),
    ("Chester A. Arthur", 1881),
    ("Grover Cleveland", 1885),
    ("Benjamin Harrison", 1889),
    ("William McKinley", 1897),
    ("Theodore Roosevelt", 1901),
    ("William Howard Taft", 1909),
    ("Woodrow Wilson", 1913),
    ("Warren G. Harding", 1921),
    ("Calvin Coolidge", 1923),
    ("Herbert Hoover", 1929),
    ("Franklin D. Roosevelt", 1933),
    ("Harry S. Truman", 1945),
    ("Dwight D. Eisenhower", 1953),
    ("John F. Kennedy", 1961),
    ("Lyndon B. Johnson", 1963),
    ("Richard Nixon", 1969),
    ("Gerald Ford", 1974),
    ("James Carter", 1977),
    ("Ronald Reagan", 1981),
    ("George H. W. Bush", 1989),
    ("William J. Clinton", 1993),
    ("George W. Bush", 2001),
    ("Barack Obama", 2009),
    ("Donald Trump", 2017),
    ("Joseph R. Biden Jr.", 2021)
]

class PresidentsGame:
    def __init__(self, presidents):
        self.presidents = presidents
        self.current_president = None
        self.options = []
        self.score = 0
        self.remaining_presidents = list(presidents)

    def start_game(self):
        self.next_question()

    def next_question(self):
        if self.remaining_presidents:
            self.current_president = random.choice(self.remaining_presidents)
            self.remaining_presidents.remove(self.current_president)
            self.options = random.sample(self.presidents, 3)
            self.options.append(self.current_president)
            random.shuffle(self.options)
            self.update_ui()
        else:
            self.show_final_score()

    def update_ui(self):
        label.config(text="Who was the U.S. President in {}?".format(self.current_president[1]))
        for i in range(4):
            buttons[i].config(text=self.options[i][0])

    def check_answer(self, selected_president):
        if self.current_president is not None and selected_president == self.current_president[0]:
        #if selected_president == self.current_president[0]:
            self.score += 1
        self.next_question()

    def show_final_score(self):
        label.config(text="Game Over! Your score: {}".format(self.score))

# Create the main window
root = tk.Tk()
root.title("U.S. Presidents Game")

# Create the game instance
game = PresidentsGame(presidents)

# Create UI elements
label = tk.Label(root, text="Who was the U.S. President in 1789?")
label.pack(pady=10)

buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=40, height=3, command=lambda i=i: game.check_answer(buttons[i].cget("text")))
    button.pack(pady=5)
    buttons.append(button)

start_button = tk.Button(root, text="Start Game", width=20, height=2, command=game.start_game)
start_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
