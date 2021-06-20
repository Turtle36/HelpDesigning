import tkinter
import tkinter.messagebox

def main():
    mainform = tkinter.Tk()
    mainform.wm_title("Internalium")
    mainform.wm_geometry("250x250+0+0")

    var = tkinter.StringVar()
    var.set("Internalium...")

    def kosongkan():
        tkinter.messagebox.showinfo("Informasi", "Mengosongkan..")
        var.set("")
    def ambilteks():
        tkinter.messagebox.showinfo("Informasi", "Mengambil...")

    e = tkinter.Entry(mainform, textvariable=var)
    e.grid(row=1, column=0, columnspan=2,
           sticky=tkinter.W+tkinter.E,
           padx=4, pady=4)
    b1 = tkinter.Button(mainform, text="Kosongkan",
                        command=kosongkan)
    b1.grid(row=2, column=0,padx=4, pady=4)


    b2 = tkinter.Button(mainform, text="Ambil",
                        command=ambilteks)
    b2.grid(row=2, column=1,padx=4, pady=4)

    mainform.mainloop()

if __name__ == '__main__':
    main()
