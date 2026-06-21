import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("main")


def topwin():
    top = tk.Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = tk.Label(top, text="this is toplevel window")
    l2.pack()

    top.mainloop()

l = tk.Label(root, text="This is root window")
btn = tk.Button(root, text="click here to open another window", command=topwin)                            

l.pack()
btn.pack()

root.mainloop()
