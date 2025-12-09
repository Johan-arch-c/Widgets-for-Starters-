import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x200")

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

title_label = tk.Label(window, text="Widgets for Starters!", font=("Arial", 14))
title_label.pack(pady=10)

entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

calc_button = tk.Button(window, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

result_label = tk.Label(window, text="Product: ")
result_label.pack(pady=5)

window.mainloop()
