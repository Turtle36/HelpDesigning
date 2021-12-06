from tkinter import *

root = Tk()
root.geometry("750x650")
root['background'] = "Cadet Blue"

lbl = Label(root, text="Welcome", padx=300,pady=30, font= (None, 60), bd=15, bg="Powder Blue", relief=GROOVE)
lbl['state'] = NORMAL
lbl.pack()
root.mainloop()