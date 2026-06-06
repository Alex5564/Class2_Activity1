import tkinter as tk 

root = tk.Tk()
root.title("Demo Window")

label = tk.Label(root, text="Hello, World!", bg = "yellow", fg = "red", height = 3, width = 20)
label.pack()

button = tk.Button(root, text="Click Me!", bg = "blue", fg = "white", height = 2, width = 10)
button.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()