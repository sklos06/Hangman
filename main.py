import random
from tkinter import *
from hangman import Hangman

GAME_WIDTH = 1000
GAME_HEIGHT = 600

def random_word():
    with open("words.txt","r") as file:
        line = file.read().splitlines()
    return random.choice(line)

class Application:
    def __init__(self, w):
        self.window = w

    def create_menu(self):
        Label(self.window, text="Hi. Let's play Hangman!", bg="white", font=("Arial", 40)).pack(side=TOP)
        Button(self.window, text="Play", height=2, width=10, command=lambda: start_game(self.window)).pack(padx=50,
                                                                                                           pady=100)


def start_game(w):
    for widgets in w.winfo_children():
        widgets.destroy()
    hangman = Hangman(w, random_word())
    hangman.create_panels()


if __name__ == '__main__':
    window = Tk()
    window.title("Hangman")
    window.config(bg="white")
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    x = int((SCREEN_WIDTH / 2) - (GAME_WIDTH / 2))
    y = int((SCREEN_HEIGHT / 2) - (GAME_HEIGHT / 2))
    window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")
    app = Application(window)

    app.create_menu()
    window.mainloop()
