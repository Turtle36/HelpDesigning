import tkinter
from tkinter import *

t = tkinter.Tk()
t.wm_geometry("250x61")
t['background'] = "Navy"

var = tkinter.StringVar()
var.set("Python...")

e1 = tkinter.Entry(t, width=40, textvariable=var)
e1.grid(row=0, column=0, columnspan=2)

import tkinter.messagebox
def clearEntry(*args):
    var.set("")
    tkinter.messagebox.showinfo("Fawwaz Apps", "Kosongkan...")

b1 = tkinter.Button(t, text="Kosongkan", bg='Powder Blue', command=clearEntry)
b1.grid(row=1, column=0, sticky=tkinter.W+tkinter.E, padx=4, pady=4)

b2 = tkinter.Button(t,  text="Ambil", bg='Powder Blue')
b2.grid(row=1, column=1, sticky=tkinter.W+tkinter.E, padx=4, pady=4)

t.mainloop()