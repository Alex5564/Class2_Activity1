import tkinter as tk

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")


def calculate():
    p = float(entry_p.get())
    t = float(entry_t.get())
    r = float(entry_r.get())

    si = (p * t * r) / 100
    ci = p * ((1 + r / 100) ** t) - p

    label_si_result.config(text=str(si))
    label_ci_result.config(text=str(ci))


lbl1 = tk.Label(root, text="Principal:")
lbl1.pack()
entry_p = tk.Entry(root)
entry_p.pack()

lbl2 = tk.Label(root, text="Time (Years):")
lbl2.pack()
entry_t = tk.Entry(root)
entry_t.pack()

lbl3 = tk.Label(root, text="Rate (%):")
lbl3.pack()
entry_r = tk.Entry(root)
entry_r.pack()

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack()

lbl4 = tk.Label(root, text="Simple Interest:")
lbl4.pack()
label_si_result = tk.Label(root, text="0.0")
label_si_result.pack()

lbl5 = tk.Label(root, text="Compound Interest:")
lbl5.pack()
label_ci_result = tk.Label(root, text="0.0")
label_ci_result.pack()

root.mainloop()
