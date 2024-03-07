from tkinter import *
import random


class Game:
    def __init__(self, master):
        self.master = master
        self.create_start_button()

    def create_start_button(self):
        self.start_button = Button(self.master, text="Start", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.start_button.destroy()  # Remove the start button
        self.create_choice_buttons()
    
    def create_choice_buttons(self):
        self.rock_button = Button(self.master, text="Rock", command=lambda: [self.show_choice("Rock"), self.show_opponent_choice()])
        self.rock_button.pack()

        self.paper_button = Button(self.master, text="Paper", command=lambda: [self.show_choice("Paper"), self.show_opponent_choice()])
        self.paper_button.pack()

        self.scissors_button = Button(self.master, text="Scissors", command=lambda: [self.show_choice("Scissors"), self.show_opponent_choice()])
        self.scissors_button.pack()

    def show_choice(self, choice):
        self.remove_choice_buttons()
        self.choice_label = Label(self.master, text="You chose " + choice)
        self.choice_label.pack()
    
    def show_opponent_choice(self):
        options = ["Rock", "Paper", "Scissors"]
        random_option = random.choice(options)
        self.opponent_label = Label(self.master, text="Your opponent chose " + random_option)
        self.opponent_label.pack()

    def remove_choice_buttons(self):
        self.rock_button.destroy()
        self.paper_button.destroy()
        self.scissors_button.destroy()


window = Tk() 
window.geometry("500x500")
window.title("Rock, Paper, Scissors")  

new_game = Game(window)

window.mainloop()