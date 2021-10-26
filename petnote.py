from tkinter.constants import ANCHOR, BOTH, CENTER, END, INSERT, LEFT, NW, RIGHT, SINGLE, TOP, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
import random
from PIL import ImageTk, Image
import pandas as pd


def petnote(petname):
    
    def ok():
        ws.destroy()
    
    ws = tk.Tk()
    ws.wm_geometry("612x384")

    ws.eval('tk::PlaceWindow . center')
    # frame = tk.Frame(ws)
    # frame.pack(side = TOP, fill = BOTH, expand = True)
    # Create canvas
    C = tk.Canvas(ws, bg="#ffc6ff", height=500, width=500)
    C.pack(fill=BOTH, expand=True)

    filename = tk.PhotoImage(file = "MyPaint2.png", master = ws)
    C.create_image(0, 0, image = filename, anchor='nw')

    # Function to resize the window
    def resize_image(e):
        global image, resized, image2
        # open image to resize it
        image = Image.open("MyPaint2.png")
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized, master = ws)
        C.create_image(0, 0, image=image2, anchor='nw')
    
    # Bind the function to configure the parent window
    C.bind("<Configure>", resize_image)

    label1Font1 = ('Maiandra GD', 15)
    label = tk.Label(C, bg = "#ffadad", font = label1Font1, text = petname + " : Thank you so much for feeding me! \n The more you feed me, \n the healthier I can be! \n Please visit me everyday or I'll be hungry!")
    label.pack(padx=10, pady=50)


    label1Font2 = ('Maiandra GD', 13)
    b = tk.Button(C, text = 'Got it!', font=label1Font2, bg = '#F9D1D1', command = ok)
    b.pack(padx=100, pady=30)

    ws.mainloop()
