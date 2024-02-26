import tkinter as tk
from api import RandomWords


class Gui(tk.Tk):
    def __init__(self) -> None:
        self.words = RandomWords()
        self.window = tk.Tk()
        self.window.geometry("700x200")

        title_label = tk.Label(text="Typing Speed Test")
        title_label.grid(column=1, row=0)

        words_label = tk.Label(text="Words: ")
        words_label.grid(column=0, row=2)
        
        
        words_text = tk.Label(text=f"{self.words.all_words()}")
        words_text.grid(column=1, row=2)


        self.words_enter = tk.Entry(width=100)
        self.words_enter.grid(column=1, row=3, pady=20)
        
        self.highscore = tk.Label(text="HIGHSCORE: ")
        self.highscore.grid(column=0,row=0)

        self.timer = tk.Label(text="TIMER: ")
        self.timer.grid(column=0, row=1)
        
        
        start_button = tk.Button(text="Start Test", width=10, command=self.get_words)
        start_button.grid(column=1, row=4)
        
        
            
    def get_words(self):
        user_input = self.words_enter.get()
        print(user_input)


