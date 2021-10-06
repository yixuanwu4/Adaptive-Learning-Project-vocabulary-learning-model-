import tkinter as tk

master = tk.Tk()

scrollbar = tk.Scrollbar(master)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(master, yscrollcommand=scrollbar.set)
for i in range(20):
    listbox.insert(tk.END, str(i))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

master.mainloop()