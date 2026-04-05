import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Display
display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Buttons layout
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            action = calculate
        else:
            action = lambda x=btn: click(x)

        tk.Button(frame, text=btn, font=("Arial", 16),
                  command=action).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(root, text="C", font=("Arial", 16), bg="red", fg="white",
          command=clear).pack(fill="both", padx=10, pady=5)

# Run app
root.mainloop()