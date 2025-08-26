# 📄 Smart Document Parser

A **Streamlit-based web application** for extracting text and analyzing documents using **Optical Character Recognition (OCR)** and **Named Entity Recognition (NER)**.  
The app supports both **images (PNG, JPG, JPEG)** and **PDF documents**, making it a lightweight but powerful tool for text extraction and entity recognition.

---

## ✨ Features
- Upload **images (PNG, JPG, JPEG)** or **PDF files**.
- Extract text using **Tesseract OCR**.
- Perform **Named Entity Recognition (NER)** with **spaCy**.
- Display:
  - Uploaded file (preview for images).
  - Extracted text.
  - Identified entities in tabular format.
- User-friendly **web interface** powered by Streamlit.

---

## 📋 Prerequisites
- **Python 3.8+**
- **Tesseract OCR** installed:
  - **Windows:** Update the path in `app/ocr.py`  
    Example:  
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```
  - **Linux (Debian/Ubuntu):**
    ```bash
    sudo apt-get install tesseract-ocr
    ```
  - **macOS (Homebrew):**
    ```bash
    brew install tesseract
    ```
- **Poppler** (required for PDF support):  
  - **Windows:** Download from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) and add `/bin` folder to PATH.  
  - **Linux/macOS:**  
    ```bash
    sudo apt-get install poppler-utils   # Debian/Ubuntu
    brew install poppler                 # macOS
    ```

---

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd smart-document-parser

2. python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

3. pip install -r requirements.txt

4. python -m spacy download en_core_web_sm

5. streamlit run ui.py


