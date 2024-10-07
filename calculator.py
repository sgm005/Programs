import tkinter as tk

def calculate():
    # Get the expression from the entry box
    expression = entry.get()

    # We'll use a try-except block to handle any errors, like dividing by zero
    try:
        # Eval evaluates the string expression. It's a quick way to handle basic math.
        result = eval(expression)
        label_result.config(text=f"Result: {result}")
    except ZeroDivisionError:
        # Handle division by zero separately, since that's common in calculators
        label_result.config(text="Can't divide by zero!")
    except:
        # For any other errors, we'll just say it's invalid
        label_result.config(text="Invalid input")

# This is the setup for the Tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# A little bit of window padding to make it look nice, but not too fancy
root.geometry("300x200")
root.config(padx=20, pady=20)

# Adding an entry box where the user can type their expression
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to trigger the calculation, we'll keep it simple
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=5)

# A label to display the result, it'll update with each calculation
label_result = tk.Label(root, text="Result will appear here", font=("Arial", 12))
label_result.pack(pady=10)

# If someone decides to press Enter instead of clicking the button
root.bind('<Return>', lambda event: calculate())

# This line isn't strictly necessary, but it's good practice to run the main loop at the end
root.mainloop()