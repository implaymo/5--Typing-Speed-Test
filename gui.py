import tkinter as tk
from tkinter import END
from api import RandomWords
from timer import Clock


class Gui(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.words = RandomWords()
        self.clock = Clock(60)
        self.geometry("1000x400")

        title_label = tk.Label(text="Typing Speed Test")
        title_label.grid(column=1, row=0)

        words_label = tk.Label(text="Words: ")
        words_label.grid(column=0, row=2)
        
        
        self.words_text = tk.Label(text=f"{self.words.all_words(self.words.words_list)}")
        self.words_text.grid(column=1, row=2)


        self.words_enter = tk.Entry(width=100)
        self.words_enter.grid(column=1, row=3, pady=20)
        
        self.highscore = tk.Label(text="HIGHSCORE: ")
        self.highscore.grid(column=0,row=0)

        self.timer = tk.Label(text=f"TIMER: {self.clock.duration}")
        self.timer.grid(column=0, row=1)
        
        self.start_test = tk.Button(text="Start Test", width=10, command=self.start_timer)
        self.start_test.grid(column=1, row=4)
        
        self.errors_label = tk.Label(text="Errors commited: ")
        self.errors_label.grid(column=0, row=5)

        self.bind("<space>", self.delete_user_answer) 
         

            
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
            self.errors_commited = self.check_errors(correct_words.split(), self.user_input.split())
            self.errors_label.config(text=f"Errors commited: {"/".join(self.errors_commited)}")
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
        self.errors = [value for value in user_answer if value not in game_words]
        return self.errors
    
    
    def update_timer(self):
        remaining_time = round(self.clock.time_remaining())
        self.timer.config(text=f"TIMER: {remaining_time}")
        if remaining_time > 0:
            self.after(1000, self.update_timer)
        else:
            self.timer.config(text="Time's up!")
        
    
    
    def start_timer(self):
        self.clock.start()
        self.update_timer()
