from turtle import *
from tkinter import *
import time


class Hangman:

    def __init__(self, w, word):
        self.typed = StringVar()
        self.window = w
        self.HANGMAN_WIDTH = 500
        self.HANGMAN_HEIGHT = 500
        self.mistakes = 0
        self.used_letters = []
        self.guessed_fields = 0
        self.word = word.upper()
        self.tab_letters = []
        self.keyboard = []
        self.keyboard_letters = (
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z")

    def __delete__(self, instance):
        print("deleted")
        for widgets in self.window.winfo_children():
            widgets.destroy()

    def create_panels(self):
        self.lb_typed = Label(self.window, text="Typed letters:", bg="white", font=("Arial", 20))
        self.lb_typed.grid(row=0, column=0)
        Label(self.window, textvariable=self.typed, bg="white").grid(row=1, column=0)
        self.frame_word = Frame(self.window, width=200, height=50, borderwidth=0)
        self.frame_word.grid(row=2, column=0)
        for i in range(len(self.word)):
            self.tab_letters.append(Label(self.frame_word, text="_", font=("Arial", 20), bg="white", padx=10))
            self.tab_letters[i].grid(row=0, column=i)
        self.canvas = Canvas(self.window, width=self.HANGMAN_WIDTH, height=self.HANGMAN_HEIGHT)
        self.canvas.grid(row=0, column=1, rowspan=3)
        self.turtle = RawTurtle(self.canvas)

        self.frame_keybord = Frame(self.window, height=200, width=10000)
        self.frame_keybord.grid(row=3, column=0)
        row = 0
        column = 0
        for i in range(26):
            self.keyboard.append(Button(self.frame_keybord, text=self.keyboard_letters[i], width=4, height=2,
                                        command=lambda l=self.keyboard_letters[i]: self.__check_letter(l)))
            self.keyboard[i].grid(row=row, column=column)
            column += 1
            if self.keyboard_letters[i] == "M":
                row = 1
                column = 0

    def __check_letter(self, letter):

        for btn in self.keyboard:
            if btn["text"] == letter:
                btn.config(state="disabled")

        if letter not in self.used_letters:
            if letter in self.word:
                self.__show_letter(letter)
                self.__check_word()
            else:
                self.mistakes += 1
                self.__draw_hangman()
                self.used_letters.append(letter)
                self.typed.set(self.used_letters)

    def __show_letter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.guessed_fields += 1
                self.tab_letters[i].config(text=letter)

    def __check_word(self):
        if self.guessed_fields == len(self.word):
            self.__delete__(self)
            play_again(self.window, "You won!")

    def __draw_hangman(self):
        self.turtle.color('black')
        self.turtle.pensize(5)
        self.turtle.penup()
        self.turtle.shape('blank')

        match self.mistakes:
            case 1:
                self.turtle.goto(-30, -40)
                self.turtle.pendown()
                self.turtle.goto(30, -40)
                self.turtle.penup()
            case 2:
                self.turtle.goto(0, -40)
                self.turtle.pendown()
                self.turtle.goto(0, 200)
                self.turtle.penup()
            case 3:
                self.turtle.goto(0, 200)
                self.turtle.pendown()
                self.turtle.goto(100, 200)
                self.turtle.penup()
            case 4:
                self.turtle.goto(100, 200)
                self.turtle.pendown()
                self.turtle.goto(100, 160)
                self.turtle.penup()
            case 5:
                self.turtle.goto(100, 120)
                self.turtle.pendown()
                self.turtle.circle(20)
                self.turtle.penup()
            case 6:
                self.turtle.goto(100, 120)
                self.turtle.pendown()
                self.turtle.goto(100, 60)
                self.turtle.penup()
            case 7:
                self.turtle.goto(100, 110)
                self.turtle.pendown()
                self.turtle.goto(80, 60)
                self.turtle.penup()
            case 8:
                self.turtle.goto(100, 110)
                self.turtle.pendown()
                self.turtle.goto(120, 60)
                self.turtle.penup()
            case 9:
                self.turtle.goto(100, 60)
                self.turtle.pendown()
                self.turtle.goto(80, 0)
                self.turtle.penup()
            case 10:
                self.turtle.goto(100, 60)
                self.turtle.pendown()
                self.turtle.goto(120, 0)
                self.turtle.penup()
                time.sleep(2)
                self.__delete__(self)
                play_again(self.window, "You lose")


def play_again(w, result):
    Label(w, text=result, font=("Arial", 50), bg="white").pack(side=TOP)
    Button(w, text="Play again", height=2, width=10, command=lambda: new_game(w)).pack(padx=50, pady=100)


def new_game(w):
    for widgets in w.winfo_children():
        widgets.destroy()
    hangman = Hangman(w, "dsa")
    hangman.create_panels()
