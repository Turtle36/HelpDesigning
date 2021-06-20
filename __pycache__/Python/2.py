from tkinter import *

d = Tk()
d.title("Fawwaz Apps")
d.geometry("750x750")
d['background'] = "Cadet Blue"

v = Frame(d, bg="Powder Blue", bd=10, width=500, height=500, relief=RIDGE)
v.grid(row=1, column=0)

f = Button(v, bg='Gold', height=5, width=10, text="1")
f.grid(row=2, column=4)

f = Button(v, bg='Gold', height=5, width=10, text="2")
f.grid(row=2, column=5)

f = Button(v, bg='Gold', height=5, width=10, text="3")
f.grid(row=2, column=6)

f = Button(v, bg='Gold', height=5, width=10, text="4")
f.grid(row=3, column=4)

f = Button(v, bg='Gold', height=5, width=10, text="5")
f.grid(row=3, column=5)

f = Button(v, bg='Gold', height=5, width=10, text="6")
f.grid(row=3, column=6)

f = Button(v, bg='Gold', height=5, width=10, text="7")
f.grid(row=4, column=4)

f = Button(v, bg='Gold', height=5, width=10, text="8")
f.grid(row=4, column=5)

f = Button(v, bg='Gold', height=5, width=10, text="9")
f.grid(row=4, column=6)

d = Entry(v, width=40)
d.grid(row=1, column=4, columnspan=4)

d.mainloop()