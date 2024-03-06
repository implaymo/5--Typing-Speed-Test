import tkinter as tk
from tkinter import END
from api import RandomWords
from timer import Clock
from type_speed import Speed


class Gui(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.words = RandomWords()
        self.clock = Clock()
        self.speed = Speed()
        
        self.geometry("1000x600")
        self.custom_font = ("Helvetica", 16)

        title_label = tk.Label(text="Typing Speed Test", font=self.custom_font)
        title_label.grid(column=1, row=0)

        words_label = tk.Label(text="Words: ", font=self.custom_font)
        words_label.grid(column=0, row=2)
        
        
        self.words_text = tk.Label(text=f"{self.words.all_words(self.words.words_list, word_index=0)}", font=self.custom_font)
        self.words_text.grid(column=1, row=2)


        self.words_enter = tk.Entry(width=100, justify='center')
        self.words_enter.grid(column=1, row=3, pady=20)
        self.words_enter.focus_set()

        
        self.score = tk.Label(text="SCORE: 0", font=self.custom_font)
        self.score.grid(column=0,row=1)
        
        
        self.highscore = tk.Label(text=f"HIGHSCORE: {self.speed.typing_high_score()}", font=self.custom_font)
        self.highscore.grid(column=0, row=0)
        
        
        self.timer = tk.Label(text=f"TIMER: {self.clock.duration}", font=self.custom_font)
        self.timer.grid(column=0, row=2)
        
        self.start_test = tk.Button(text="Restart", width=10, command=self.restart_game)
        self.start_test.grid(column=1, row=4)
        
        self.errors_label = tk.Label(text="Errors commited: ", font=self.custom_font)
        self.errors_label.grid(column=0, row=5)


        self.time_started = False
        self.time_ended = False

        self.all_errors = []
        self.total_words = 0 
        self.count_errors = 0

        self.bind("<space>", self.handles_space_key) 
         

            
    def get_words_user(self):
        self.user_input = self.words_enter.get().lower().strip()
        if self.user_input:
            self.check_words()
            self.words.words_list.pop(0)

    def check_words(self):
        word_index = 0
        game_words = self.words.all_words(self.words.words_list, word_index=0).split()
        user_answer = self.user_input
        word_checked = game_words[word_index].lower()
        
        if word_checked is None:
            self.words = RandomWords()
        
        if user_answer == word_checked:
            self.handles_success()
            word_index += 1
            self.update_word(word_index=word_index)
        else:
            # Adds all errors to the list all_errors and shows the words without being in a list
            self.all_errors.append("".join(self.check_errors(game_words, user_answer)))
            self.handles_failure()
            word_index += 1
            self.update_word(word_index=word_index)
            
    def delete_user_answer(self, event=None):
        self.words_enter.delete(0, END)
     

        
    def handles_success(self):
        self.total_words += 1
        print("SUCCESS")
        
    
    def handles_failure(self):
        self.total_words -= 1
        self.count_errors += 1
        print("Missed something")
    
    
    def check_errors(self, game_words, user_answer):        
        errors = [value for value in user_answer if value not in game_words]
        return errors
    
    def handles_space_key(self, event=None):
        if self.time_started is True:
            self.get_words_user()
            self.delete_user_answer()
        else:
            self.handles_start_game()
    
    def update_timer(self):
        remaining_time = round(self.clock.time_remaining())
        self.timer.config(text=f"TIMER: {remaining_time}", font=self.custom_font)
        if remaining_time > 0:
            self.after(1000, self.update_timer)
        else:
            self.time_ended = True
            self.timer.config(text="Time's up!", font=self.custom_font)
            self.handles_end_game()
        
    
    def handles_start_game(self):
        self.time_started = True
        self.clock.start()
        self.update_timer()
        self.speed.typing_high_score()
        self.get_words_user()
        self.delete_user_answer()
        
    def handles_end_game(self):
        if self.time_ended is True:
            self.errors_label.config(text=f"Errors commited: {self.count_errors}\n{'\n'.join(self.all_errors)}", font=self.custom_font)
            self.disable_entry_widget()
            self.score.config(text=f"SCORE: {self.speed.typing_speed_result(self.total_words, self.clock.start_time)}", font=self.custom_font)
            if self.speed.new_highscore is True:
                self.highscore.config(text=f"NEW HIGHSCORE {self.speed.typing_high_score()} 🥳", font=self.custom_font)
        
    def disable_entry_widget(self):
        self.words_enter.config(state=tk.DISABLED)
    
    def enable_entry_widget(self):
        self.words_enter.config(state=tk.NORMAL)
        

    
    def update_word(self, word_index):
        return self.words_text.config(text=f"{self.words.all_words(self.words.words_list, word_index=word_index)}")
    
    def restart_game(self):
        self.enable_entry_widget()
        return self.handles_start_game()