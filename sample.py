"""Pick the CET4_edited.txt, CET6_edited.txt, TOEFL_abridged.txt as data to categorize the user English level 
(resource: https://github.com/mahavivo/english-wordlists), """
# After knowing the level of words which the user aims for practice, then pick the corresponded vocabulary list set.
# After practicing 50 words everyday, provide a small paragraph of reading material for the user to practice.

from tkinter.constants import ANCHOR, END, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk


def select_channel():

    def ok():
        ws.destroy()

    ws = tk.Tk()

    # Define a label for the list.  
    label = tk.Label(ws, text = "Which level of vocabulary do you wish to practice?") 
    label.pack()

    ws.title('Adaptive Learning')
    ws.geometry('400x400')
    ws.config(bg='#446644')
    var = tk.StringVar(ws)


    lb = tk.Listbox(ws)
    lb.pack()
    lb.insert(0, 'CET4')
    lb.insert(1, 'CET6')
    lb.insert(2, 'TOEFL')


    def selected_item():
        
        # Traverse the tuple returned by
        # curselection method and print
        # corresponding value(s) in the listbox
        for i in lb.curselection():
            global choice 
            choice = lb.get(i)

    tk.Button(ws, text='Save my choice', command=selected_item).pack(pady=20)
    show = tk.Label(ws)
    show.pack()

    button = tk.Button(ws, text="OK", command=ok)
    button.pack()

    ws.mainloop()

# --- main ---

select_channel()
print(choice)


def extract_words (cet4, cet6, toefl):
    cet4words = []
    cet6words = []
    toeflwords = []

    with io.open(cet4, mode="r", encoding="utf-8") as f:
        next(f)
        next(f)
        for line in f:
            cet4words.append(line.split())
    with io.open(cet6, mode="r", encoding="utf-8") as f:
        next(f)
        next(f)
        for line in f:
            cet6words.append(line.split())
    with io.open(toefl, mode="r", encoding="utf-8") as f:
        next(f)
        next(f)
        for line in f:
            toeflwords.append(line.split())
    return (cet4words, cet6words, toeflwords)

cet4words, cet6words, toeflwords = extract_words ('CET4_edited.txt', 'CET6_edited.txt', 'TOEFL_abridged.txt')

# target = answers["size"]

if choice == "CET4":
    print(cet4words)
elif  choice == "CET6":
    print(cet6words)
else:
    print(toeflwords)