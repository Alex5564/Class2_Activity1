import tkinter as tk
import random

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = f"Tie! Both chose {user_choice}."
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = f"You Win! {user_choice} beats {computer_choice}."
    else:
        result = f"You Lose! {computer_choice} beats {user_choice}."
    
    result_label.config(text=result)

instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12))
instructions.pack(pady=20)

tk.Button(root, text="Rock", width=15, command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=30)

root.mainloop()
