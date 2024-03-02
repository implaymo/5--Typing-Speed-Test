import tkinter as tk
from tkinter import END
from api import RandomWords
from timer import Clock


class Gui(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.words = RandomWords()
        self.clock = Clock(10)
        self.geometry("1000x400")

        title_label = tk.Label(text="Typing Speed Test")
        title_label.grid(column=1, row=0)

        words_label = tk.Label(text="Words: ")
        words_label.grid(column=0, row=2)
        
        
        self.words_text = tk.Label(text=f"{self.words.all_words(self.words.words_list)}")
        self.words_text.grid(column=1, row=2)


        self.words_enter = tk.Entry(width=100, justify='center')
        self.words_enter.grid(column=1, row=3, pady=20)
        self.words_enter.focus_set()

        
        self.highscore = tk.Label(text="HIGHSCORE: ")
        self.highscore.grid(column=0,row=0)

        self.timer = tk.Label(text=f"TIMER: {self.clock.duration}")
        self.timer.grid(column=0, row=1)
        
        self.start_test = tk.Button(text="Start Test", width=10)
        self.start_test.grid(column=1, row=4)
        
        self.errors_label = tk.Label(text="Errors commited: ")
        self.errors_label.grid(column=0, row=5)


        self.time_started = False
        self.time_ended = False

        self.all_errors = []

        self.bind("<space>", self.handles_space_key) 
         

            
    def get_words_user(self):
        self.user_input = self.words_enter.get().lower().strip()
        if self.user_input:
            self.user_input = ''.join(self.user_input)
            self.check_words()


    def check_words(self):
        correct_words = self.words.all_words(self.words.words_list)
        if self.user_input == correct_words:
            self.handles_success()
        else:
            # Adds all errors to the list all_errors and shows the words without being in a list
            self.all_errors.append("/".join(self.check_errors(correct_words.split(), self.user_input.split())))
            self.handles_failure()

            
        self.generate_new_words()

    def delete_user_answer(self, event=None):
        self.words_enter.delete(0, END)
     
    
    def generate_new_words(self):
        new_words = RandomWords()
        self.words.words_list = new_words.words_list
        self.words_text.config(text=f"{self.words.all_words(self.words.words_list)}")
        
    def handles_success(self):
        print("SUCCESS")
        
    
    def handles_failure(self):
        print("Missed something")
    
    
    def check_errors(self, game_words, user_answer):        
        errors = [value for value in user_answer if value not in game_words]
        return errors
    
    def handles_space_key(self, event=None):
        if self.time_started is True:
            self.get_words_user()
            self.delete_user_answer()
        else:
            self.start_timer()

    def handles_end_game(self):
        if self.time_ended is True:
            self.errors_label.config(text=f"Errors commited: \n{"\n".join(self.all_errors)}")

    
    def update_timer(self):
        remaining_time = round(self.clock.time_remaining())
        self.timer.config(text=f"TIMER: {remaining_time}")
        if remaining_time > 0:
            self.after(1000, self.update_timer)
        else:
            self.time_ended = True
            self.timer.config(text="Time's up!")
            self.handles_end_game()
        
    
    
    def start_timer(self):
        self.time_started = True
        self.clock.start()
        self.update_timer()
