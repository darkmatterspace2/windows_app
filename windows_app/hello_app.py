import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello Windows App")
root.geometry("300x150")  # Width x Height

# Add a label
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=40)

# Run the app
root.mainloop()
