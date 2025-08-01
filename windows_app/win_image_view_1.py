import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 400), Image.Resampling.LANCZOS)  # Resize to fit window
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference

# Create window
root = tk.Tk()
root.title("Basic Image Viewer")
root.geometry("500x500")

# Button to open image
btn = tk.Button(root, text="Open Image", command=open_image)
btn.pack(pady=10)

# Label to show image
image_label = tk.Label(root)
image_label.pack(pady=10)

# Run the app
root.mainloop()
