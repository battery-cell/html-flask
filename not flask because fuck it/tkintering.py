from tkinter import *
from tkinter import messagebox
windowed = Tk()
windowed.title("hello world")
windowed.geometry("400x400")
def definition():
    messagebox.showwarning("Warning")
button1 = Button(windowed, text="click me",command=definition)
button1.place(x=150,y=0)
windowed.mainloop()