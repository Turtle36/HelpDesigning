from tkinter import *

print(d)
root = Tk()
root.title("Fawwaz Apps")
root['background'] = "Navy"
v = IntVar()
Radiobutton(root, text='Python', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Java', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='C++', variable=v, value=3).pack(anchor=W)
root.mainloop()