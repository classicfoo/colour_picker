import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab

def get_hex_color(event):
    # Get the color of the pixel at the click position
    x, y = event.x, event.y
    rgb = image.getpixel((x, y))
    hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
    # Display the color
    color_label.config(text=f"Hex Color: {hex_color}")
    color_label.config(bg=hex_color)
    # Update the current color
    global current_color
    current_color = hex_color

def paste_image(event=None):
    try:
        # Get image from clipboard and convert it to a format Tkinter can use
        global image
        image = ImageGrab.grabclipboard()
        image.thumbnail((400, 400))  # Resize if image is too large
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=photo, anchor='nw')
        canvas.image = photo  # Keep a reference
    except:
        messagebox.showerror("Error", "No image found in clipboard!")

def copy_color_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(current_color)
    messagebox.showinfo("Copied", f"Copied {current_color} to clipboard")

# Set up the GUI
root = tk.Tk()
root.title("Color Picker App")

paste_button = tk.Button(root, text="Paste Image", command=paste_image)
paste_button.pack()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind("<Button-1>", get_hex_color)

color_label = tk.Label(root, text="Hex Color:", font=("Arial", 14))
color_label.pack(side=tk.LEFT)

copy_button = tk.Button(root, text="Copy", command=copy_color_to_clipboard)
copy_button.pack(side=tk.RIGHT)

# Bind Ctrl+V for pasting image
root.bind('<Control-v>', paste_image)

current_color = ""  # Variable to hold the current color
root.mainloop()
