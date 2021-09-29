"""Pick the CET4_edited.txt, CET6_edited.txt, TOEFL_abridged.txt as data to categorize the user English level 
(resource: https://github.com/mahavivo/english-wordlists), """
# After knowing the level of words which the user aims for practice, then pick the corresponded vocabulary list set.
# After practicing 50 words everyday, provide a small paragraph of reading material for the user to practice.

from tkinter.constants import ANCHOR, BOTH, CENTER, END, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
from game import Dog
from PIL import ImageTk, Image


def select_channel():

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

    filename = tk.PhotoImage(file = "/home/nauxiy/Workspace/Adaptive learning/Term project + paper/data/MyPaint1.png")
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
    label1Font = ("Brush Script Std", 20, "bold")
    label = tk.Label(C, bg = "pink", font=label1Font, text = " Which level of vocabulary do you wish to practice? ") 
    label.pack(padx=10, pady=10)


    # Create the list box
    lb = tk.Listbox(C, font = 40)
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

    tk.Button(C, text='Save my choice', font = 40, command=selected_item).pack(pady=20)
    show = tk.Label(C)
    show.pack()

    button = tk.Button(C, text="OK", font = 50, command=ok)


    button.pack()




    ws.mainloop()



select_channel()
print(choice)


# target = answers["size"]

