import tkinter as tk

def check_strength():
    try:
        length = int(entry.get())
        
        if length <= 5:
            result_label.config(text="Strength: Weak", fg="red")
        elif 6 <= length <= 8:
            result_label.config(text="Strength: Medium", fg="yellow")
        elif 9 <= length <= 12:
            result_label.config(text="Strength: Strong", fg="light green")
        else: # length > 12
            result_label.config(text="Strength: Very Strong", fg="dark green")
    except ValueError:
        result_label.config(text="Please enter a valid number", fg="white")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#2c3e50")

instruction_label = tk.Label(root, text="Enter Password Length:", bg="#2c3e50", fg="white")
instruction_label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_strength, bg="#34495e", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#2c3e50")
result_label.pack(pady=30)

root.mainloop()
