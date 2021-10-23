# Page 6 feeds food to the user selected pet
# The food fed to the pet is redeemed by the equivalent amount of words memorized by the user
from tkinter.constants import ANCHOR, BOTH, CENTER, END, INSERT, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import Label, messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
from PIL import ImageTk, Image

class food():

    def select_channel(self, petname, pet, goal):

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

        if pet=="dog":
            petbuttonphoto = Image.open("dog.png")
            petbuttonphoto = petbuttonphoto.resize((200,150), Image.ANTIALIAS)
            petbuttonphoto = ImageTk.PhotoImage(petbuttonphoto)
        else:
            petbuttonphoto = Image.open("cat.png")
            petbuttonphoto = petbuttonphoto.resize((200,150), Image.ANTIALIAS)
            petbuttonphoto = ImageTk.PhotoImage(petbuttonphoto)

        def printtext():
            from petnote import petnote
            petnote(petname)

        pickpet = tk.Button(C, bg="yellow", command = printtext, text = 'Click Me!', compound = "left", image = petbuttonphoto).place(x=70, y=170)
        

        words = ["The food fed to the pet is redeemed \n by the equivalent amount of words memorized by the you today! ", "Your pet:", petname, " received ", str(goal), " snacks today! ", petname, " is very happy! \n" + "Please come back and feed your pet again tomorrow!"]
        colours = ["black", "black", "blue", "black", "green", "black", "blue", "black"]

        label1Font = ("Baskerville Old Face", 20)
        for index,word in enumerate(words):
            if index == 0:
                label = tk.Label(C, anchor = CENTER, bg = '#2a9d8f', text = word, font=label1Font, fg=colours[index])
                label.pack(padx=10, pady=50)
            else:
                label = tk.Label(C, anchor = CENTER, bg = '#e76f51', text = word, font=label1Font, fg=colours[index])
                label.pack(pady = 10)

        tk.Button(C, text='Finish today\'s learning :D', bg = '#e9c46a', font = label1Font, command=ok).pack(pady=20)

        
        # # Define a label for the list.  
        
        # label = tk.Label(C, anchor = CENTER, bg = '#F9D1D1', font=label1Font, text = "The food fed to the pet is redeemed \n by the equivalent amount of words memorized by the you today! \n " + petname + " received " + str(goal) + " snacks today! \n " + petname + " is very haapy! \n" + "Please come back and feed your pet again tomorrow!" ) 
        # label.pack(padx=10, pady=100)

        ws.mainloop()

# petname = "Robin"
# goal = 5
# food1 = food()
# pet="cat"
# food1.select_channel(petname, pet, goal)