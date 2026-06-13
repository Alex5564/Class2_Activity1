from tkinter import *
from tkinter import messagebox

root = Tk()

messagebox.showinfo("Information", "Welcome")

btn = Button(root, text="Click Me", command=lambda: messagebox.showinfo("Information", "Button Clicked"))
btn.pack()

root.mainloop()