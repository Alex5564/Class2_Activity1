import tkinter as tk


def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2

    txt_result.delete("1.0", tk.END)
    txt_result.insert(tk.END, f"Result: {product}")


root = tk.Tk()
root.geometry("400x300")

root.title("Getting Started with Widgets")

lbl_desc = tk.Label(root, text="This app multiplies two numbers together.")
lbl_desc.pack(pady=10)

lbl1 = tk.Label(root, text="Enter First Number:")
lbl1.pack()
entry1 = tk.Entry(root)
entry1.pack()

lbl2 = tk.Label(root, text="Enter Second Number:")
lbl2.pack()
entry2 = tk.Entry(root)
entry2.pack()

btn_calc = tk.Button(root, text="Calculate Product", command=multiply)
btn_calc.pack(pady=15)

txt_result = tk.Text(root, width=30, height=2)
txt_result.pack()

root.mainloop()
