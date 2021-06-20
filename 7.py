import random
import tkinter
d = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
f1 = random.choice(d)
f2 = random.choice(d)
f3 = random.choice(d)
f4 = random.choice(d)
f5 = random.choice(d)
d = tkinter.Tk()
d.title("fawwaz apps")
d['background'] = "Navy"
from tkinter import *
j = tkinter.Label(d, font= (None, 60), bd=5, bg="#0a4477", relief=RIDGE)
j.pack()

hg = tkinter.Label(d,pady=20,text='      ', font= (None, 60), bd=5, bg="#0a4477", relief=RIDGE)
hg.pack()

l = tkinter.Label(j)
l['text'] = "Random Number 10-100"
l['background'] = "#0a4578"
l.pack()

f = tkinter.Label(j)
f['text'] = "1.", f1
f['background'] = "Blue"
f.pack()
f = tkinter.Label(j)
f['text'] = "2.", f2
f['background'] = "Navy"
f.pack()
f = tkinter.Label(j)
f['text'] = "3.", f3
f['background'] = "Cyan"
f.pack()
f = tkinter.Label(j)
f['text'] = "4.", f4
f['background'] = "Royal Blue"
f.pack()
f = tkinter.Label(j)
f['text'] = "5.", f5
f['background'] = "Cadet Blue"
f.pack()
d.mainloop()
