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


# This class takes the user daily goal number to randomly select amount of words from the selected vocabulary list
class Page3():

    def __init__(self):
          # this is an instance variable.
          self.somevar2 = 0

    def select_channel(self, goal, choice):

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
        label = tk.Label(C, bg = '#F9D1D1', font=label1Font, text = " Now let's start learning! \n Here are your words for today!") 
        label.pack(padx=20, pady=30)

        # Pick the right vocabulary list
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
        wordslist = []
        if choice == "CET4":
            wordslist = cet4words
        elif  choice == "CET6":
            wordslist = cet6words
        else:
            wordslist = toeflwords

        # Now to get the settled amount of words from the list
        # def getdailywords(wordslist):
        tageswords = random.sample(wordslist, goal)
        print(tageswords)

        ### Next step to save daily words into a file with data
        ### then add gamification factors into the word memorizing part
        ### meow meow meow food food 

        # Convert the tageswords into a string
        wordsstring = ''
        for words in tageswords:
            tmp = '\t'.join(words) + '\n'
            wordsstring = wordsstring+tmp

        # Save tageswords into a file with data
        # The file name will be the date when the saved words are learned
        time = datetime.datetime.now()
        template = '%Y-%m-%d'
        time_string = time.strftime(template)
        save_path = '/home/nauxiy/Workspace/Adaptive learning/Term project + paper/data/oldwords'
        completePath = os.path.join(save_path, time_string + ".txt") 
        with open(completePath, 'w') as f:
            f.write(wordsstring)
        
        labelall = {}
        
        for x, eachword in enumerate(tageswords):
            labelall[x] = tk.Label(C,font = label1Font, text = eachword, bg = "#ffb4a2")
            labelall[x].pack(pady = 30)

        ws.mainloop()
        
        return tageswords
            



# x = Page3()
# choice="CET4"
# goal = 5
# print(x.select_channel(goal, choice))




