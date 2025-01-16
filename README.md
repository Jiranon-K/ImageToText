# ImageToText

**ImageToText** is a Python-based GUI application for extracting text from images using OCR (Optical Character Recognition). The app provides an easy-to-use interface that allows users to select an image file, extract the text, and copy the results to their clipboard. Built with Tkinter, PIL, and pytesseract, this tool is perfect for converting images to text.

---

## Features
- **Simple GUI**: Intuitive and user-friendly design.
- **Image to Text Conversion**: Extract text from popular image formats such as `.png`, `.jpg`, and `.jpeg`.
- **Clipboard Support**: Copy the extracted text directly to your clipboard.
- **Enhanced Accuracy**: Grayscale conversion and sharpening improve OCR results.
- **Tesseract OCR Integration**: Leverages Tesseract’s robust OCR capabilities.

---

## Requirements

Before using the application, ensure you have the following installed:

### Dependencies
- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Required Python Libraries:
  - `tkinter`
  - `Pillow`
  - `pytesseract`

---



## Usage

### Step 1: Run the Application
```bash
python main.py
```

### Step 2: Use the GUI
1. Click the **SELECT IMAGE** button.
2. Choose an image file from your file explorer.
3. View the extracted text in the output window.
4. Copy the text using the **COPY** button.

---

## How It Works
1. **Image Selection**:
   - Users select an image using a file dialog.
   - Supported formats: `.png`, `.jpg`, `.jpeg`.

2. **Preprocessing**:
   - The image is converted to grayscale for better OCR performance.
   - A sharpening filter is applied to enhance text clarity.

3. **Text Extraction**:
   - Tesseract OCR processes the image and extracts text.
   - Configuration (`--oem 3 --psm 6`) ensures high accuracy for English text.

4. **Output**:
   - The extracted text is displayed in a text box.
   - Users can copy the text directly to the clipboard.

---


## Acknowledgments
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Python Pillow Library](https://python-pillow.org/)



