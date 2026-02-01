import tkinter as tk

# Function to handle button clicks
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main GUI Window
root = tk.Tk()
root.title("Simple Calculator")

# Entry Widget for Display
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons Layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for row_index, row in enumerate(buttons, start=1):
    for col_index, text in enumerate(row):
        button = tk.Button(
            root, text=text, font="Arial 15", height=2, width=5,
            relief=tk.RAISED, borderwidth=3
        )
        button.grid(row=row_index, column=col_index, padx=5, pady=5)
        button.bind("<Button-1>", button_click)

# Start GUI Mainloop
root.mainloop()
