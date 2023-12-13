import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import torch
from torchvision import transforms

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x200")
        self.root.iconbitmap('Desktop')
        self.setup_ui()

    def setup_ui(self):
        # Creates a button in the window
        self.button = Button(self.root, text="Click Me", command=self.button_clicked, padx=10, pady=10)
        self.button.pack()

    def button_clicked(self):
        # Open method used to open an image file
        file_path = "/Users/sam/Downloads/Pictures/1.jpeg"
        self.show_image(file_path)

    def show_image(self, file_path):
        # Open image file and show it in a label
        img = Image.open(file_path)
        img = img.resize((150, 150), Image.ANTIALIAS)

        # Convert the PIL Image to a PyTorch Tensor
        transform = transforms.Compose([transforms.ToTensor()])
        tensor_image = transform(img)

        # Convert the PyTorch Tensor back to a PIL Image for display
        img = transforms.ToPILImage()(tensor_image)

        img = ImageTk.PhotoImage(img)

        image_label = Label(self.root, image=img)
        image_label.image = img  # Keep a reference to avoid garbage collection
        image_label.pack()

if __name__ == "__main__":
    # Creates our window
    window = tk.Tk()
    # Create the app instance
    app = ImageViewerApp(window)
    # Presents the root
    window.mainloop()
