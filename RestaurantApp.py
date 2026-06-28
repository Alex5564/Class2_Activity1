import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "Fries Meals": 2,
            "Lunch Meals": 2,
            "Burger Meals" : 3,
            "Pizza Meals" : 4,
            "Cheese Burger" : 2.5,
            "Drinks " : 1,
            }

        self.exchange_rates = 82

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text= "Restaurant Management App",
            font=("Arial", 20, "bold"),
        ).grid(row=0, column = 0, columnspan=2, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12),
            )
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12),
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5,
        )




        

