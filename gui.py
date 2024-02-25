import tkinter as tk
from api import RandomWords


class Gui():
    words = RandomWords()
    window = tk.Tk()

    window.geometry("700x200")


    title_label = tk.Label(text="Typing Speed Test")
    title_label.grid(column=1, row=0)

    words_label = tk.Label(text="Words: ")
    words_label.grid(column=0, row=2)
    
    
    words_text = tk.Label(text=f"{words.all_words_printed()}")
    words_text.grid(column=1, row=2)

    words_entry = tk.Entry(width=100)
    words_entry.grid(column=1, row=3, pady=20)
    
    highscore = tk.Label(text="HIGHSCORE: ")
    highscore.grid(column=0,row=0)

    timer = tk.Label(text="TIMER: ")
    timer.grid(column=0, row=1)
    
    
    start_button = tk.Button(text="Start Test", width=10)
    start_button.grid(column=1, row=4)
    
    


    window.mainloop()


    