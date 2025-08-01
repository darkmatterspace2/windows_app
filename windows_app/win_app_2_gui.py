import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Greeting", "You clicked the button!")

# Main window
root = tk.Tk()
root.title("Enhanced Hello App")
root.geometry("300x180")

# Label
label = tk.Label(root, text="Hello, World!", font=("Segoe UI", 16))
label.pack(pady=20)

# Button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

# Run the app
root.mainloop()
