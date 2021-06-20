import tkinter
from tkinter import *

t = Tk()
t.title("Internalium")

var = StringVar()
var.set("Text...")

k = Label(t, relief=SUNKEN, bd=10)
k.grid(row=1, column=0)

k2 = Label(t, relief=SUNKEN, bd=10)
k2.grid(row=0, column=0)

e = Entry(k2, textvariable=var, width=40, bg="#fffff2")
e.grid(row=2, column=1, columnspan=2)
def clear():
    var.set("")

def open_nitro_type():
    import webbrowser
    webbrowser.open_new_tab("https://nitrotype.com/")

b1 = Button(k, text="Clear", command=clear, bd=4, bg="Gray")
b1.grid(row=3, column=1, sticky=tkinter.W+tkinter.E, padx=4, pady=4, ipadx=38)

bq = Button(k, text="Exit", command=quit, bd=4, bg="Gray")
bq.grid(row=3, column=2 ,sticky=tkinter.W+tkinter.E, padx=4, pady=4, ipadx=38)

b2 = Button(k, text="", command=open_nitro_type, bg="Yellow")
b2.grid(row=3, column=3 ,sticky=tkinter.W+tkinter.E)

b3 = Button(k, text="", command=open_nitro_type, bg="YELLOw")
b3.grid(row=3, column=0 ,sticky=tkinter.W+tkinter.E)

t.mainloop()