from tkinter.constants import ANCHOR, BOTH, CENTER, END, INSERT, LEFT, NW, RIGHT, SINGLE, W, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
import random
from typing_extensions import IntVar
from PIL import ImageTk, Image
import datetime
import os.path
import pandas as pd


# This class takes the user daily goal number to randomly select amount of words from the selected vocabulary list
class Page3():

    def __init__(self):
          # this is an instance variable.
          self.somevar2 = 0

    def select_channel(self, tageswords):

        def ok():
            ws.destroy()

        ws = tk.Tk()
        ws.wm_geometry("1024x768")


        ws.title('Adaptive Learning')
        frame = tk.Frame(ws)
        frame.pack(side = LEFT, fill = BOTH, expand = True)

        # Create canvas
        C = tk.Canvas(frame, bg="pink", height=768, width=1024)
        C.pack(fill=BOTH, expand=True)

        filename = tk.PhotoImage(file = "/home/nauxiy/Workspace/Adaptive learning/Term project + paper/data/MyPaint1.png", master = ws)
        C.create_image(0, 0, image = filename, anchor='nw')

        # Function to resize the window
        def resize_image(e):
            global image, resized, image2
            # open image to resize it
            image = Image.open("/home/nauxiy/Workspace/Adaptive learning/Term project + paper/data/MyPaint1.png")
            # resize the image with width and height of root
            resized = image.resize((e.width, e.height), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(resized)
            C.create_image(0, 0, image=image2, anchor='nw')
        
        # Bind the function to configure the parent window
        frame.bind("<Configure>", resize_image)
        
        # Define a label for the list.  
        label1Font = ("Baskerville Old Face", 20)
        label = tk.Label(C, bg = '#F9D1D1', font=label1Font, text = " Now let's test how much you learned :)") 
        label.pack(padx=20, pady=30)


        # Convert the tageswords into a string
        wordsstring = ''
        for words in tageswords:
            tmp = '\t'.join(words) + '\n'
            wordsstring = wordsstring+tmp
        
        words_meaning = {}
        
        for x, eachword in enumerate(tageswords):
            words_meaning[eachword[0]] = eachword[-1] 
            

        def questions(words_meaning):
            v = tk.IntVar()
            tk.Label(text = "Q: What is the meaning of this word",font=("arial",12,"bold")).place(x=10,y=50)
            tk.Radiobutton(text=words_meaning[0],font=("arial",12),variable = v, value=words_meaning[0]).pack(anchor = W)
            tk.Radiobutton(text=words_meaning[1],font=("arial",12),variable = v, value=words_meaning[1]).pack(anchor = W)
            tk.Radiobutton(text=words_meaning[2],font=("arial",12),variable = v, value=words_meaning[2]).pack(anchor = W)
            tk.Radiobutton(text=words_meaning[3],font=("arial",12),variable = v, value=words_meaning[3]).pack(anchor = W)
        questions(words_meaning)
        ws.mainloop()
        
        return tageswords
            



x = Page3()

tageswords=[['rest', 'n.剩余部分；其余的人'], ['operator', '[ˈɔpəreitə]', 'n.操作人员，接线员'], ['oven', '[ˈʌvən]', 'n.炉，灶；烘箱'], ['friendship', '[ˈfrend∫ip]', 'n.友谊，友好'], ['tool', '[tuːl]', 'n.工具，器具，用具']]

x.select_channel(tageswords)




