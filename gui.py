import tkinter as tk
from tkinter import * 


class Gui():
    window = tk.Tk()

    window.geometry("300x200")


    title_label = tk.Label(text="Typing Speed Test")
    title_label.grid(column=1, row=0)

    words_label = tk.Label(text="Words: ")
    words_label.grid(column=0, row=1)

    words_entry = tk.Entry(width=30)
    words_entry.grid(column=1, row=2)


    start_button = tk.Button(text="Start Test", width=10)
    start_button.grid(column=1, row=4)
    
    


    window.mainloop()


    