import tkinter
from tkinter import *

r = int(input("Masukkan Angka: "))

t = Tk()
t.title("Internalium")
t['background'] = "Royal Blue"

for z in range(r):
    l1 = Label(t, text="O", font = (70), bd = 10, bg="Navy",relief=SOLID, justify=LEFT, height=2, width=5, foreground="Cyan")
    l1.grid(row=z, column=z)


t.mainloop()