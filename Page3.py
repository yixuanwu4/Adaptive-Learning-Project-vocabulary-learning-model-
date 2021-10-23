from tkinter.constants import ANCHOR, BOTH, CENTER, END, FLAT, HORIZONTAL, INSERT, LEFT, NW, RIGHT, SINGLE, TOP, VERTICAL, W, Y, YES
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


# Page3 takes the user daily goal number to randomly select amount of words from the selected vocabulary list
# The picked and learned words will be removed from the original dictionary and saved in another folder for review
# For words whose definitions exceed the width of the listbox, use the right side key to see more
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
        label = tk.Label(C, bg = '#b5e48c', highlightthickness=10,  bd = 10, font=label1Font, text = " Now let's start learning! \n Here are your words for today!") 
        label.pack(padx=20, pady=30)

        b = tk.Button( C, text = 'I have finished learning them!', font=label1Font, bg = '#F9D1D1', command = ok, anchor = W)
        b.configure(width = 50, activebackground = "#33B5E5", relief = FLAT)
        
        b.pack(side = tk.BOTTOM, padx=50, pady = 50)

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

        # Convert the tageswords into a string
        wordsstring = ''
        for words in tageswords:
            tmp = '\t'.join(words) + '\n'
            wordsstring = wordsstring+tmp

        # The following commented trunk removed the selected words from the original dictionary
        # To test the following codes, please use the files in folder "some test files"
        """targetdict = choice+"_edited.txt"
        with open(targetdict, "r") as fp:
            lines = fp.readlines()

        with open(targetdict, "w") as fp:
            for i, line in enumerate(lines):
                # seperate each line into parts so I can get the first item in this line
                oneline = line.strip("\n")
                newoneline = oneline.split()
                # go through each word in the tageswords list
                for items in tageswords:
                    # pick the first English word in this item and compare with the first one of first item in the line
                    if items[0] == newoneline[0]:
                        # if these two are different then keep this line in the file
                        print(items[0], newoneline[0])
                        del lines[i]

        new_file = open("CET6_edited1.txt", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()"""



        # Save tageswords into a file with data
        # The file name will be the date when the saved words are learned
        # So the user can review the words and the newly selected words won't be replicated with the old words
        time = datetime.datetime.now()
        template = '%Y-%m-%d'
        time_string = time.strftime(template)
        save_path = '/home/nauxiy/Workspace/Adaptive learning/Term project + paper/data/oldwords'
        completePath = os.path.join(save_path, time_string + ".txt") 
        with open(completePath, 'w') as f:
            f.write(wordsstring)
        

        # It's better to put the "daily learning words" in a scroll bar
        # because the number of words a user might set as the daily goal can be different
        scrollbarY = tk.Scrollbar(C, orient=VERTICAL, width=20 )
        scrollbarY.pack(side="right", fill = tk.Y)
        listbox = tk.Listbox(C, width = 50, selectmode=tk.SINGLE, highlightthickness=10,  bd=10, height = 50, justify=CENTER)
        for i in range(len(tageswords)):
            listbox.insert(tk.END, tageswords[i])
        
        listbox.configure(background="#fde2e4", foreground="#14213d", font=('Courier 18'), yscrollcommand=scrollbarY.set, width=0, height=0, justify = LEFT)
        scrollbarY.config(command=listbox.yview)
        listbox.pack(padx=10, pady=10)



        ws.mainloop()
        
        return tageswords
            



# x = Page3()
# choice="CET6"
# goal = 50
# print(x.select_channel(goal, choice))




