from tkinter.constants import ANCHOR, BOTH, CENTER, END, INSERT, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
from game import Dog
from PIL import ImageTk, Image
from Page5 import Page5Dog, Page5Cat

p5Dog = Page5Dog()
p5Cat = Page5Cat()

# Page 4 asks the user to determine which pet he/she wants to select

class Page4():
    def __init__(self):
          # this is an instance variable.
          self.somevar2 = 0

    def select_channel(self, *args):

        def ok():
            ws.destroy()

        ws = tk.Tk()
        ws.wm_geometry("1024x768")


        ws.title('Adaptive Learning')
        frame = tk.Frame(ws)
        frame.pack(side = LEFT, fill = BOTH, expand = True)

        # Create canvas
        C = tk.Canvas(frame, bg="pink", height=788, width=1024)
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
        
                
        # Creating and resizing a photoimage object to use image 
        dogbuttonphoto = Image.open("dog.png")
        dogbuttonphoto = dogbuttonphoto.resize((400,300), Image.ANTIALIAS)
        dogbuttonphoto = ImageTk.PhotoImage(dogbuttonphoto)

        catbuttonphoto = Image.open("cat.png")
        catbuttonphoto = catbuttonphoto.resize((400,300), Image.ANTIALIAS)
        catbuttonphoto = ImageTk.PhotoImage(catbuttonphoto)

        # Adding widgets to the root window
        tk.Label(C, text = 'Congratulations on completing your daily task! \n Now as your reward, \n please pick the animal which you wanna keep as a pet!', font =(
        'Verdana', 25)).pack(side = tk.TOP, pady = 10)

        
        def nextPageDog():
            ws.destroy()
            p5Dog.select_channel()
            global petname
            petname = 'dog'
        

        def nextPageCat():
            ws.destroy()
            p5Cat.select_channel()
            global petname
            petname = 'cat'

        # here, image option is used to
        # set image on button
        pickdog = tk.Button(C, text = 'Click Me !', image = dogbuttonphoto, command = nextPageDog).pack(padx=15, pady=20)
        pickcat = tk.Button(C, text = 'Click Me !', image = catbuttonphoto, command = nextPageCat).pack(padx=15, pady=20)

        ws.mainloop()

        if petname == 'dog':
            return p5Dog.getname()
        else:
            return p5Cat.getname()

        
            
  
# x = Page4()
# x.select_channel(x)

        
