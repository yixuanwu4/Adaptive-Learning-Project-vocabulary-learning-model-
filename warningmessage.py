from tkinter.constants import ANCHOR, BOTH, CENTER, END, LEFT, NW, RIGHT, SINGLE, Y, YES
from tkinter import messagebox
import io
import tkinter as tk
from tkinter import messagebox
from tkinter.font import families
from PIL import ImageTk, Image

def warningmessage():
    def ok():
        ws.destroy()
    
    ws = tk.Tk()
    ws.wm_geometry("300x300")

    ws.eval('tk::PlaceWindow . center')
    # Create canvas
    C = tk.Canvas(ws, bg="#ED5538", height=300, width=300)
    C.pack(fill=BOTH, expand=True)

    label1Font1 = ('Maiandra GD', 15)
    label = tk.Label(C, font = label1Font1, text = " Please type in only numbers! ")
    label.pack(padx=10, pady=30)


    label1Font2 = ('Maiandra GD', 13)
    b = tk.Button(C, text = 'okay!', font=label1Font2, bg = '#F9D1D1', command = ok)
    b.pack(padx=100, pady=30)

    ws.mainloop()

warningmessage()