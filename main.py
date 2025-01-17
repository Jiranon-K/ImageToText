import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def set_tesseract_path():
    file_path = filedialog.askopenfilename(
        title="Select Tesseract Executable",
        filetypes=[("Executable Files", "*.exe")]
    )
    if file_path:
        try:
            pytesseract.pytesseract.tesseract_cmd = file_path
            messagebox.showinfo("Success", "Tesseract path set successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to set Tesseract path: {e}")

def open_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if file_path:
        try:
            image = Image.open(file_path)
            image = image.convert("L")
            image = image.filter(ImageFilter.SHARPEN)

            config = '--oem 3 --psm 6'
            extracted_text = pytesseract.image_to_string(image, lang='eng', config=config)

            show_text_window(extracted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot read the file: {e}")

def show_text_window(text):
    text_window = tk.Toplevel(root)
    text_window.title("Text Output")
    text_window.geometry("1200x800")
    text_window.configure(bg="#F7F7F7")

    text_label = tk.Label(
        text_window, text="Extracted Text:", font=("Arial", 14, "bold"), bg="#F7F7F7"
    )
    text_label.pack(pady=(10, 5))

    text_box = tk.Text(text_window, wrap=tk.WORD, font=("Arial", 12))
    text_box.insert(tk.END, text)
    text_box.configure(state=tk.NORMAL, relief=tk.GROOVE, bd=2)
    text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))

    copy_button = tk.Button(
        text_window, text="COPY TEXT", font=("Arial", 12, "bold"),
        bg="#4CAF50", fg="white", activebackground="#45A049", activeforeground="white",
        command=lambda: copy_to_clipboard(text)
    )
    copy_button.pack(pady=10)

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    messagebox.showinfo("Success", "Text copied to clipboard successfully!")

root = tk.Tk()
root.title("Extract Text from Image")
root.geometry("300x250")
root.configure(bg="#EFEFEF")

header_label = tk.Label(
    root, text="Image to Text Converter", font=("Arial", 16, "bold"), bg="#EFEFEF", fg="#333333"
)
header_label.pack(pady=(20, 10))

set_path_button = tk.Button(
    root, text="SET TESSERACT PATH", font=("Arial", 12, "bold"), bg="#f39c12", fg="white",
    activebackground="#d35400", activeforeground="white", command=set_tesseract_path
)
set_path_button.pack(pady=(10, 10), ipadx=10, ipady=5)

open_button = tk.Button(
    root, text="SELECT IMAGE", font=("Arial", 12, "bold"), bg="#008CBA", fg="white",
    activebackground="#005F73", activeforeground="white", command=open_image
)
open_button.pack(pady=(10, 20), ipadx=10, ipady=5)


root.mainloop()



