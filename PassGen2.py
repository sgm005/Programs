import string
import random
import tkinter as tk
from tkinter import messagebox

# Password generator function
def pass_generator(length, caps, numbers, symbols):
    letter = string.ascii_lowercase

    if caps:
        letter += string.ascii_uppercase
    if numbers:
        letter += string.digits
    if symbols:
        letter += string.punctuation

    password = ''.join(random.choice(letter) for _ in range(length))
    return password

# Function to get inputs and generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Error", "8 characters or more are needed.")
            return
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number.")
        return

    caps = caps_var.get()
    numbers = numbers_var.get()
    symbols = symbols_var.get()

    new_password = pass_generator(length, caps, numbers, symbols)
    messagebox.showinfo("New Password", f"Your new password is: {new_password}")
    print(f"Your new password is: {new_password}")

# Create the Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Inputs for the password settings
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=15, pady=15)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

caps_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=caps_var).grid(row=1, column=0, padx=10, pady=10)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=1, column=1, padx=10, pady=10)

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=2, column=0, padx=10, pady=10)

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=1, padx=15, pady=15)

# Run the app
root.mainloop()