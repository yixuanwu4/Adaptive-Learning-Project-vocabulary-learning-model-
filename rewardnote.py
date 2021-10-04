from tkinter.constants import ANCHOR, BOTH, CENTER, END, INSERT, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
import random
from PIL import ImageTk, Image
import datetime
import os.path
import pandas as pd

def rewardnote():
    
    def ok():
        ws.destroy()
    
    ws = tk.Tk()
    ws.wm_geometry("800x500")

    ws.eval('tk::PlaceWindow . center')
    # Create canvas
    C = tk.Canvas(ws, bg="#ffc6ff", height=500, width=800)
    C.pack(fill=BOTH, expand=True)

    label1Font1 = ('Maiandra GD', 15)
    label = tk.Label(C, bg = "#ffadad", font = label1Font1, text = " After you reach the daily goal, you will get some amazing presents! \n Now let's start the learning! ")
    label.pack(padx=0, pady=30)


    label1Font2 = ('Maiandra GD', 13)
    b = tk.Button(C, text = 'Got it!', font=label1Font2, bg = '#F9D1D1', command = ok)
    b.pack(padx=100, pady=30)

    ws.mainloop()

rewardnote()
