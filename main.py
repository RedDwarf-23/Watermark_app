# Add watermark to your images with this simple app

from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

window = Tk()
window.title("Watermark Adding App")
window.minsize(width=500, height=300)

def get_unique_filename(directory, base_name, extension):
    """Generate a unique filename in the specified directory."""
    i = 1
    while os.path.exists(f"{directory}/{base_name}_{i}{extension}"):
        i += 1
    return f"{directory}/{base_name}_{i}{extension}"

def upload():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

    try:
        # Open the selected image
        image = Image.open(filename)

        # Open the watermark image
        image_watermark = Image.open("redwarf_watermark.png")

        # Paste the watermark onto the original image
        image.paste(image_watermark, (0, 0), mask=image_watermark)
        image.show()

        # Ensure the save directory exists
        save_dir = "C:/Users/Urvashi/PycharmProjects/Watermark_app/watermark_images"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Generate a unique filename for the watermarked image
        unique_filename = get_unique_filename(save_dir, "watermarked_image", ".png")
        image.save(unique_filename)
        print(f"Watermarked image saved at: {unique_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


# UI Setup
website_label = Label(text="Upload your image to add watermark")
website_label.pack()

upload_button = Button(text="upload", width=36, command=upload)
upload_button.pack(pady=10)

image_label = Label(window)
image_label.pack()

window.mainloop()
