import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

THUMBNAIL_SIZE = (100, 100)

def load_images_from_folder(folder_path):
    for widget in gallery_frame.winfo_children():
        widget.destroy()  # Clear previous thumbnails

    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

    row, col = 0, 0
    for img_name in images:
        img_path = os.path.join(folder_path, img_name)
        try:
            img = Image.open(img_path)
            img.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            thumb_label = tk.Label(gallery_frame, image=photo, cursor="hand2")
            thumb_label.image = photo  # Prevent garbage collection
            thumb_label.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col == 5:
                col = 0
                row += 1
        except Exception as e:
            print(f"Failed to load {img_name}: {e}")

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        load_images_from_folder(folder_path)

# Main window
root = tk.Tk()
root.title("Image Gallery Viewer")
root.geometry("600x500")

# Select folder button
select_btn = tk.Button(root, text="Select Image Folder", command=choose_folder)
select_btn.pack(pady=10)

# Scrollable canvas for thumbnails
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

gallery_frame = scrollable_frame  # alias for clarity

# Run app
root.mainloop()
