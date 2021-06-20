import tkinter
import tkinter.messagebox

def main():
    windows = tkinter.Tk()
    windows['background'] = "#345733"
    windows.wm_title("internalium")

    def onclick():
        tkinter.messagebox.askyesno("Question", "3 X 3 is 6?")

    b1 = tkinter.Button(windows, text="BUTTON-1",
                        background="Orange",
                        foreground="Yellow",
                        activeforeground="Orange",
                        activebackground="Yellow",
                        command=onclick)
    b1.pack()

    windows.mainloop()

if __name__ == '__main__':
    main()





















