import tkinter as tk

def convert_length():
    try:
        meters = float(entry_input.get())
        feet = meters * 3.28084
        label_result.config(text=f"{feet:.2f} Feet")
    except ValueError:
        label_result.config(text="Enter a number")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#e0f7fa") 

label_title = tk.Label(root, text="Meters to Feet Converter", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="#006064")
label_title.pack(pady=30)

entry_input = tk.Entry(root, font=("Arial", 14), width=15, justify="center")
entry_input.pack(pady=10)
entry_input.insert(0, "1")

btn_convert = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#00838f", fg="white", command=convert_length)
btn_convert.pack(pady=20)

label_result = tk.Label(root, text="3.28 Feet", font=("Arial", 14, "bold"), bg="#e0f7fa", fg="#006064")
label_result.pack(pady=20)

root.mainloop()

