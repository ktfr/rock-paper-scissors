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
        self.start_button.destroy() 
        self.create_select_label()
        self.create_choice_buttons()

    def create_select_label(self):
        self.select_label = Label(self.master, text="Please select your weapon:")
        self.select_label.pack()
    
    def create_choice_buttons(self):
        self.rock_button = Button(self.master, text="Rock", command=lambda: [self.show_choice("Rock"), 
                                                                             self.show_opponent_choice(), 
                                                                             self.calculate_final_result()])
        self.rock_button.pack()

        self.paper_button = Button(self.master, text="Paper", command=lambda: [self.show_choice("Paper"), 
                                                                               self.show_opponent_choice(),
                                                                               self.calculate_final_result()])
        self.paper_button.pack()

        self.scissors_button = Button(self.master, text="Scissors", command=lambda: [self.show_choice("Scissors"),
                                                                                     self.show_opponent_choice(),
                                                                                     self.calculate_final_result()])
        self.scissors_button.pack()

    def show_choice(self, choice):
        self.user_choice = choice 
        self.remove_choice_buttons()
        self.select_label.destroy()
        self.user_choice_label = Label(self.master, text="You chose " + choice)
        self.user_choice_label.pack()
    
    def show_opponent_choice(self):
        global options, random_option
        options = ["Rock", "Paper", "Scissors"]
        self.opponent_choice = random.choice(options)  
        self.opponent_label = Label(self.master, text="Your opponent chose " + self.opponent_choice)
        self.opponent_label.pack()

    def remove_choice_buttons(self):
        self.rock_button.destroy()
        self.paper_button.destroy()
        self.scissors_button.destroy()

    def calculate_final_result(self):
        if self.user_choice == self.opponent_choice:
            result = "It's a tie!"
        elif (self.user_choice == "Rock" and self.opponent_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.opponent_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.opponent_choice == "Paper"):
            result = "You win!"
        else:
            result = "You lose!"
        self.show_final_result(result)

    def show_final_result(self, result):
        self.result_label = Label(self.master, text=result)
        self.result_label.pack()
    
    def restart_game(self):
        pass

# Create window for Game
window = Tk() 
window.geometry("200x300")
window.title("Rock, Paper, Scissors")  

# Create a new Game instance
new_game = Game(window)

window.mainloop()