from tkinter import *
winowed = Tk()
winowed.title("hello world")
winowed.geometry("200x400")

button1 = Button(winowed, text="hello world!",)
button1.grid(row=2, column=1)
entering = Entry(winowed,font=("Arial",18), justify="left")
entering.grid(row=1, column=1)
winowed.mainloop()