import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

COLUMN_WIDTH = 200
GUTTER = 10

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        display_images(folder_path)

def display_images(folder_path):
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')
    image_paths = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(image_extensions)
    ]

    columns = [[], []]  # Two columns for now
    col_heights = [0, 0]  # Track height of each column

    for path in image_paths:
        try:
            img = Image.open(path)
            w, h = img.size
            new_w = COLUMN_WIDTH
            new_h = int(h * (new_w / w))
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            # Choose the column with the smallest height
            col_index = col_heights.index(min(col_heights))
            label = tk.Label(canvas_frame, image=photo, bg="black")
            label.image = photo  # Keep reference
            label.place(x=(col_index * (COLUMN_WIDTH + GUTTER)), y=col_heights[col_index])
            col_heights[col_index] += new_h + GUTTER
            columns[col_index].append(label)

        except Exception as e:
            print(f"Error loading {path}: {e}")

    canvas.configure(scrollregion=canvas.bbox("all"))

# GUI setup
root = tk.Tk()
root.title("Masonry Style Image Gallery")
root.geometry("500x600")
root.configure(bg="black")

# Button
btn = tk.Button(root, text="Select Image Folder", command=choose_folder)
btn.pack(pady=10)

# Scrollable Canvas
canvas = tk.Canvas(root, bg="black")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

canvas_frame = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Run
root.mainloop()
