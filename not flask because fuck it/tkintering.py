from tkinter import *
from tkinter import messagebox
windowed = Tk()
windowed.title("hello world")
windowed.geometry("400x400")
def definition():
    messagebox.showinfo("Warning", "tymon bedziwe bity")
def definition2():
    button3.place(x=150,y=40)
def definition3():
    messagebox.showerror("it is what it is", "tymon to dobry bardzo kolega")
button1 = Button(windowed, text="click me",command=definition)
button2 = Button(windowed, text="yo",command=definition2)
button3 = Button(windowed, text="hello", command=definition3)
button1.place(x=150,y=0)
button2.place(x=150, y=100)
windowed.mainloop()