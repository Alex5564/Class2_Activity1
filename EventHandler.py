from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_click(event):
    print("/nThe button was clicked!")

button = Button(window, text="Click Me")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()