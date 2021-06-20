from tkinter import *

d = Tk()
d.wm_title("Fawwaz Apps")
d.wm_geometry("750x650")
d['background'] = "Navy"

board = 8


f = Label(d,padx=40, pady=40,  text="F", font= (None, "60"), bd=board, relief=GROOVE, bg="Powder Blue")
f['state'] = NORMAL
f.grid(row=1, column=1)
f1 = Label(d,padx=40, pady=40,  text="A", font= (None, "60"), bd=board, relief=GROOVE, bg="Powder Blue")
f1['state'] = NORMAL
f1.grid(row=1, column=2)
f2 = Label(d,padx=40, pady=40,  text="W", font= (None, "60"), bd=board, relief=GROOVE, bg="Powder Blue")
f2['state'] = NORMAL
f2.grid(row=1, column=3)
"-------------------------------------------------------------------------------------------------"
f = Label(d,padx=40, pady=40,  text="W", font= (None, "60"), bd=board, relief=GROOVE, bg="Cyan")
f['state'] = NORMAL
f.grid(row=1, column=4)
f1 = Label(d,padx=40, pady=40,  text="A", font= (None, "60"), bd=board, relief=GROOVE, bg="Cyan")
f1['state'] = NORMAL
f1.grid(row=1, column=5)
f2 = Label(d,padx=40, pady=40,  text="Z", font= (None, "60"), bd=board, relief=GROOVE, bg="Cyan")
f2['state'] = NORMAL
f2.grid(row=1, column=6)
"--------------------------------------------------------------------------------------------------"
f = Label(d,padx=40, pady=40,  text="O", font= (None, "60"), bd=board, relief=GROOVE, bg="Blue")
f['state'] = NORMAL
f.grid(row=3, column=1)
f1 = Label(d,padx=40, pady=40,  text="D", font= (None, "60"), bd=board, relief=GROOVE, bg="Blue")
f1['state'] = NORMAL
f1.grid(row=3, column=2)
f2 = Label(d,padx=40, pady=40,  text="I", font= (None, "60"), bd=board, relief=GROOVE, bg="Blue")
f2['state'] = NORMAL
f2.grid(row=3, column=3)

f = Label(d,padx=40, pady=40,  text="G", font= (None, "60"), bd=board, relief=GROOVE, bg="Royal BluE")
f['state'] = NORMAL
f.grid(row=3, column=4)
f1 = Label(d,padx=40, pady=40,  text="I", font= (None, "60"), bd=board, relief=GROOVE, bg="Royal Blue")
f1['state'] = NORMAL
f1.grid(row=3, column=5)
f = Label(d,padx=40, pady=40,  text="A", font= (None, "60"), bd=board, relief=GROOVE, bg="Royal BLUE")
f['state'] = NORMAL
f.grid(row=3, column=6)

d.mainloop()