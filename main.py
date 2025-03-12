import tkinter as tk
import math

# Function to update expression
def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))

# Function to evaluate the expression
def equalpress():
    try:
        total = str(eval(entry_var.get()))
        entry_var.set(total)
        history_list.insert(tk.END, entry_var.get())
    except:
        entry_var.set("Error")

# Function to clear entry
def clear():
    entry_var.set("")

# Function for memory operations
def memory_store():
    global memory
    memory = entry_var.get()

def memory_recall():
    entry_var.set(memory)

def memory_clear():
    global memory
    memory = ""

def memory_subtract():
    global memory
    memory = str(float(memory) - float(entry_var.get()))

def memory_add():
    global memory
    memory = str(float(memory) + float(entry_var.get()))

# Function for advanced calculations
def sqrt():
    entry_var.set(str(math.sqrt(float(entry_var.get()))))

def power():
    entry_var.set(str(float(entry_var.get()) ** 2))

def sin_func():
    entry_var.set(str(math.sin(math.radians(float(entry_var.get())))))

def cos_func():
    entry_var.set(str(math.cos(math.radians(float(entry_var.get())))))

def tan_func():
    entry_var.set(str(math.tan(math.radians(float(entry_var.get())))))

def log_func():
    entry_var.set(str(math.log10(float(entry_var.get()))))

def ln_func():
    entry_var.set(str(math.log(float(entry_var.get()))))

def exp_func():
    entry_var.set(str(math.exp(float(entry_var.get()))))

def factorial_func():
    entry_var.set(str(math.factorial(int(entry_var.get()))))

def insert_pi():
    entry_var.set(entry_var.get() + str(math.pi))

def insert_e():
    entry_var.set(entry_var.get() + str(math.e))

# Creating main window
root = tk.Tk()
root.title("Advanced iPhone Style Calculator")
root.geometry("400x700")  # Reduced screen size
root.configure(bg="#1C1C1C")

entry_var = tk.StringVar()
memory = ""

# Entry field
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=0, relief=tk.FLAT, justify='right', bg="#505050", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10, sticky="nsew")

# History listbox
history_list = tk.Listbox(root, height=3, font=("Arial", 14), bg="#505050", fg="white", bd=0, relief=tk.FLAT)
history_list.grid(row=10, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Button layout
def create_button(text, row, col, bg="#333", fg="white", width=6, height=2, command=None):
    return tk.Button(root, text=text, font=("Arial", 18, "bold"), width=width, height=height, bg=bg, fg=fg, bd=0, relief=tk.RAISED, command=command).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Buttons
buttons = [
    ('MC', 1, 0, "#A5A5A5", "black", memory_clear), ('MR', 1, 1, "#A5A5A5", "black", memory_recall), ('M+', 1, 2, "#A5A5A5", "black", memory_add), ('M-', 1, 3, "#A5A5A5", "black", memory_subtract),
    ('C', 2, 0, "#A5A5A5", "black", clear), ('√', 2, 1, "#A5A5A5", "black", sqrt), ('x²', 2, 2, "#A5A5A5", "black", power), ('÷', 2, 3, "#FF9500", "white", lambda: press("/")),
    ('7', 3, 0, "#505050", "white", lambda: press("7")), ('8', 3, 1, "#505050", "white", lambda: press("8")), ('9', 3, 2, "#505050", "white", lambda: press("9")), ('×', 3, 3, "#FF9500", "white", lambda: press("*")),
    ('4', 4, 0, "#505050", "white", lambda: press("4")), ('5', 4, 1, "#505050", "white", lambda: press("5")), ('6', 4, 2, "#505050", "white", lambda: press("6")), ('-', 4, 3, "#FF9500", "white", lambda: press("-")),
    ('1', 5, 0, "#505050", "white", lambda: press("1")), ('2', 5, 1, "#505050", "white", lambda: press("2")), ('3', 5, 2, "#505050", "white", lambda: press("3")), ('+', 5, 3, "#FF9500", "white", lambda: press("+")),
    ('0', 6, 0, "#505050", "white", lambda: press("0")), ('.', 6, 1, "#505050", "white", lambda: press(".")), ('=', 6, 2, "#FF9500", "white", equalpress)
]

# Creating buttons dynamically
for text, row, col, bg, fg, command in buttons:
    create_button(text, row, col, bg, fg, command=command)

# Adjust grid weights
for i in range(11):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
