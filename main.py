from tkinter import *
from hangman import Hangman
GAME_WIDTH = 1000
GAME_HEIGHT = 600



class Application:
    def __init__(self, w):
        self.window = w

    def create_menu(self):
        Label(self.window, text="Hi. Let's play Hangman!", bg="#5e615a", fg="#FFFFFF", font=("Arial", 40, "bold")).pack(side=TOP, pady=50)
        Button(self.window, text="Play", height=2, width=10, bg="#191a18", fg="#d5dbce", bd=0, activebackground="#222421", activeforeground="#e9f0e1",
               command=lambda: start_game(self.window)).pack(pady=50)


def start_game(w):
    for widgets in w.winfo_children():
        widgets.destroy()
    hangman = Hangman(w)
    hangman.create_panels()


if __name__ == '__main__':
    window = Tk()
    window.title("Hangman")
    window.config(bg="#5e615a")
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    x = int((SCREEN_WIDTH / 2) - (GAME_WIDTH / 2))
    y = int((SCREEN_HEIGHT / 2) - (GAME_HEIGHT / 2))
    window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")
    window.iconbitmap("hangman.ico")
    app = Application(window)

    app.create_menu()
    window.mainloop()
