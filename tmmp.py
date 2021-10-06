from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image



class CapitalQuiz:

    def select_():

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
        
        # Bind the function to configure the ws window
        frame.bind("<Configure>", resize_image)


        def __init__(self,ws):
            
            self.ws = ws
            self.Welcome = Frame(self.ws)
            self.Welcome.pack(fill=BOTH,expand=1)
            
            self.TitleLabel = Label(self.Welcome, text = "Let's see how well you learned today!",
                                    bg = "black", fg = "white", font = ("Time", '14', "bold italic"))
            self.TitleLabel.pack(side=TOP,fill=X)
                
            self.NextButton = ttk.Button(self.Welcome, text = 'Next', command = self.show_Questions)
            self.NextButton.place(x=20,y=60)
            
            self.Questions = Frame(self.ws)
            
            self.QuestionsLabel = Label(self.Questions, text = "Questions",
                                        bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                        font = ("Time", '14', "bold italic"))
            self.once_done=False
            self.QuestionsLabel.pack(side=TOP,fill=X,anchor="w")
            
            Label(self.Questions, text = "Q1.  What is the capital of United States?",font=("arial",12,"bold")).place(x=10,y=50)
            self.capital_one=StringVar()
            self.capital_one.set("hellow")
            Radiobutton(self.Questions,text="Washington DC",font=("arial",12),variable=self.capital_one,value="Washington DC").place(x=20,y=80)
            Radiobutton(self.Questions,text="London",font=("arial",12),variable=self.capital_one,value="London").place(x=20,y=110)
            Radiobutton(self.Questions,text="Delhi",font=("arial",12),variable=self.capital_one,value="Delhi").place(x=20,y=140)
            Radiobutton(self.Questions,text="Tokyo",font=("arial",12),variable=self.capital_one,value="Tokyo").place(x=20,y=170)
            Label(self.Questions, text = "Q2.  What is the capital of Russia?",font=("arial",12,"bold")).place(x=10,y=200)
            self.capital_two=StringVar()
            self.capital_two.set("hellow")
            Radiobutton(self.Questions,text="Moscow",font=("arial",12),variable=self.capital_two,value="Moscow").place(x=20,y=230)
            Radiobutton(self.Questions,text="Islamabad",font=("arial",12),variable=self.capital_two,value="Islamabad").place(x=20,y=260)
            Radiobutton(self.Questions,text="Delhi",font=("arial",12),variable=self.capital_two,value="Delhi").place(x=20,y=290)
            Radiobutton(self.Questions,text="Tokyo",font=("arial",12),variable=self.capital_two,value="Tokyo").place(x=20,y=320)
            Label(self.Questions, text = "Q3.  New Delhi is the capital of which country?",font=("arial",12,"bold")).place(x=10,y=350)
            self.capital_three=StringVar()
            self.capital_three.set("hellow")
            Radiobutton(self.Questions,text="India",font=("arial",12),variable=self.capital_three,value="India").place(x=20,y=380)
            Radiobutton(self.Questions,text="Canada",font=("arial",12),variable=self.capital_three,value="Canada").place(x=20,y=410)
            Radiobutton(self.Questions,text="Japan",font=("arial",12),variable=self.capital_three,value="Japan").place(x=20,y=440)
            Radiobutton(self.Questions,text="Spain",font=("arial",12),variable=self.capital_three,value="Spain").place(x=20,y=470)
            Label(self.Questions, text = "Q4.  What is the capital of Canada?",font=("arial",12,"bold")).place(x=10,y=500)
            self.capital_four=StringVar()
            self.capital_four.set("hellow")
            Radiobutton(self.Questions,text="Ottawa",font=("arial",12),variable=self.capital_four,value="Ottawa").place(x=20,y=530)
            Radiobutton(self.Questions,text="Paris",font=("arial",12),variable=self.capital_four,value="Paris").place(x=20,y=560)
            Radiobutton(self.Questions,text="Madrid",font=("arial",12),variable=self.capital_four,value="Madrid").place(x=20,y=590)
            Radiobutton(self.Questions,text="Beijing",font=("arial",12),variable=self.capital_four,value="Beijing").place(x=20,y=620)
            Label(self.Questions, text = "Q5.  State True or False: Beijing is the capital of China?",font=("arial",12,"bold")).place(x=10,y=650)
            self.capital_five=StringVar()
            self.capital_five.set("hellow")
            Radiobutton(self.Questions,text="True",font=("arial",12),variable=self.capital_five,value="True").place(x=20,y=680)
            Radiobutton(self.Questions,text="False",font=("arial",12),variable=self.capital_five,value="False").place(x=20,y=710)
            self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
            self.HomeButton.place(x=30,y=760)
            self.SubmitButton = ttk.Button(self.Questions, text = 'Submit', command = self.submit)
            self.SubmitButton.place(x=130,y=760)
                
        def submit(self):
            count=0
            if self.capital_one.get()=="Washington DC":
                count+=1
            if self.capital_two.get()=="Moscow":
                count+=1
            if self.capital_three.get()=="India":
                count+=1
            if self.capital_four.get()=="Ottawa":
                count+=1
            if self.capital_five.get()=="True":
                count+=1
            Label(self.Questions,font=("arial",40,"bold"),text=f"You scored: {str(count)}/5").place(x=500,y=50)
            self.c=count
            self.capital_five.set("hellow")
            self.capital_four.set("hellow")
            self.capital_three.set("hellow")
            self.capital_two.set("hellow")
            self.capital_one.set("hellow")
            self.once_done=True
            self.SubmitButton.config(state=DISABLED)
            
        def show_Welcome(self):
            if self.once_done==True:
                for i in self.Questions.winfo_children():
                    i.destroy()
                self.Questions.pack_forget()
            else:
                self.Questions.pack_forget()
            self.Welcome.pack(fill=BOTH,expand=1)
            
        def show_Questions(self):
            self.Welcome.pack_forget()
            if self.once_done==True:
                self.Questions.pack(fill=BOTH,expand=1)
                Label(self.Questions,font=("arial",40,"bold"),text=f"You scored: {str(self.c)}/5").place(x=500,y=50)
                Label(self.Questions,font=("arial",30,"bold"),text="You can only attempt the quiz once.").place(x=500,y=160)
            else:
                self.Questions.pack(fill=BOTH,expand=1)

        ws.mainloop()


    

CapitalQuiz.select_()

