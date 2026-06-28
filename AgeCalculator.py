import tkinter as tk
from datetime import date

def calculate_age():
    try:
        user_name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        today = date.today()
        birth_date = date(year, month, day)
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Hello {user_name}!\nYou are {age} years old.", fg="#2E7D32")
    except ValueError:
        result_label.config(text="Please enter valid numeric date values.", fg="#D32F2F")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#F5F5F5")

header = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), bg="#F5F5F5")
header.pack(pady=20)

input_frame = tk.Frame(root, bg="#F5F5F5")
input_frame.pack()

tk.Label(input_frame, text="Name:", bg="#F5F5F5").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Date:", bg="#F5F5F5").grid(row=1, column=0, padx=10, pady=5, sticky="e")
day_entry = tk.Entry(input_frame)
day_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Month:", bg="#F5F5F5").grid(row=2, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(input_frame)
month_entry.grid(row=2, column=1, pady=5)

tk.Label(input_frame, text="Year:", bg="#F5F5F5").grid(row=3, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(input_frame)
year_entry.grid(row=3, column=1, pady=5)

calc_btn = tk.Button(root, text="Calculate Age", command=calculate_age, bg="#1976D2", fg="white", padx=10)
calc_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#F5F5F5")
result_label.pack(pady=10)

root.mainloop()