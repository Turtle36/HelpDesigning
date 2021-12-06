import tkinter
from tkinter import *
from tkinter import messagebox
def main():
    ws = Tk()
    ws.title("Fawwaz Apps")
    ws.geometry("300x250")

    def bc(*args):
        tkinter.messagebox.showinfo("Message",
                                    "%s " % entry.get())

    l1 = Label(ws, text="Masukkan Text: ")
    l1.grid(row=0, column=0)
    entry = Entry(ws, width=24)
    entry.grid(row=0, column=1)
    b1 = Button(ws, text="Selesai")
    b1.bind("<Button-1>", bc)
    b1.grid(row=1, column=1)


    menubar = Menu(ws, background='Navy', foreground='black', activebackground='white', activeforeground='black')
    file = Menu(menubar, tearoff=0, background='White', foreground='black')
    file.add_command(label="Keluar", command=ws.quit)
    menubar.add_cascade(label="Aplikasi", menu=file)

    ws.config(menu=menubar)
    ws.mainloop()
if __name__ == '__main__':
    main()