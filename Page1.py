from tkinter.constants import ANCHOR, BOTH, CENTER, END, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
from PIL import ImageTk, Image
from Page2 import Page2

p2 = Page2()

class Page1():
    def select_channel(self):


        def ok():
            ws.destroy()

        def nextPage():
            ws.destroy()
            p2.select_channel(p2)

        ws = tk.Tk()
        ws.wm_geometry("1024x768")


        ws.title('Adaptive Learning')
        frame = tk.Frame(ws)
        frame.pack(side = LEFT, fill = BOTH, expand = True)

        # Create canvas
        C = tk.Canvas(frame, bg="pink", height=768, width=1024)
        C.pack(fill=BOTH, expand=True)
        
        filename = ImageTk.PhotoImage(file = "MyPaint1.png", master=ws)
        C.create_image(0, 0, image = filename, anchor='nw')

        # Function to resize the window
        def resize_image(e):
            global image, resized, image2
            # open image to resize it
            image = Image.open("MyPaint1.png")
            # resize the image with width and height of root
            resized = image.resize((e.width, e.height), Image.ANTIALIAS)

            image2 = ImageTk.PhotoImage(resized, master = ws)
            C.create_image(0, 0, image=image2, anchor='nw')
        
        # Bind the function to configure the parent window
        frame.bind("<Configure>", resize_image)
        
        # Define a label for the list.  
        label1Font = ('Maiandra GD', 20, "bold")
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

        button = tk.Button(C, text="OK", font = 50, command=nextPage)


        button.pack()




        ws.mainloop()

    def getchoice():
        return choice

# x = Page1()
# Page1.select_channel(x)
# goal = p2.getgoal(p2)
# print(choice, goal)