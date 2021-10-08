from tkinter.constants import ANCHOR, BOTH, CENTER, END, INSERT, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
from PIL import ImageTk, Image

# Ask the user to name the pet
class Page5Dog():

    def select_channel(self, *args):

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
        label1Font = ("Baskerville Old Face", 20)
        label = tk.Label(C, bg = '#F9D1D1', font=label1Font, text = "You just selected a puppy as your learning partner! \n Now please give a cute name to your puppy!") 
        label.pack(padx=10, pady=100)

                # Receive user input
        e = tk.Entry(C, font=label1Font)
        e.pack()
        def printtext():
            global string
            string = e.get()
            ws.destroy()
        
        b = tk.Button(C, text = 'Okay! :D', font=label1Font, bg = '#F9D1D1', command = printtext)
        b.pack(padx=10, pady=100)

        ws.mainloop()
        global name
        name = string
    
    def getname(self, *args):
        return name

class Page5Cat():

    def select_channel(self, *args):

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
        label1Font = ("Baskerville Old Face", 20)
        label = tk.Label(C, bg = '#F9D1D1', font=label1Font, text = "You just selected a kitty as your learning partner! \n Now please give a cute name to your puppy!") 
        label.pack(padx=10, pady=100)

                # Receive user input
        e = tk.Entry(C, font=label1Font)
        e.pack()
        def printtext():
            global string
            string = e.get()
            ws.destroy()
        
        b = tk.Button(C, text = 'Okay! :D', font=label1Font, bg = '#F9D1D1', command = printtext)
        b.pack(padx=10, pady=100)

        ws.mainloop()
        global name
        name = string
    
    def getname(self, *args):
        return name

# x = Page5()
# x.select_channel(x)