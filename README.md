Smart Document Parser

This is a Streamlit-based web application that performs Optical Character Recognition (OCR) and Named Entity Recognition (NER) on uploaded images. The app extracts text from images using Tesseract OCR and identifies named entities using spaCy.

Features





Upload images in PNG, JPG, or JPEG formats.



Extract text from images using Tesseract OCR.



Perform Named Entity Recognition (NER) on the extracted text using spaCy.



Display the uploaded image, extracted text, and identified entities in a user-friendly interface.

Prerequisites





Python 3.8 or higher



Tesseract OCR installed on your system





For Windows, update the tesseract_cmd path in app/ocr.py to point to your Tesseract installation (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe).



For Linux/macOS, ensure Tesseract is installed and accessible in your system PATH.

Installation





Clone the repository:

git clone <repository-url>
cd smart-document-parser



Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install the required dependencies:

pip install -r requirements.txt



Install Tesseract OCR:





Windows: Download and install from Tesseract at UB Mannheim.



Linux: sudo apt-get install tesseract-ocr



macOS: brew install tesseract

Usage





Run the Streamlit app:

streamlit run ui.py



Open your browser and navigate to http://localhost:8501.



Upload an image (PNG, JPG, or JPEG).



View the extracted text and named entities displayed on the page.

Project Structure

smart-document-parser/
├── app/
│   ├── __init__.py
│   ├── ocr.py          # OCR functionality using Tesseract
│   ├── ner.py          # NER functionality using spaCy
├── uploads/            # Directory to store uploaded images
├── ui.py               # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore file

Dependencies

Listed in requirements.txt:





streamlit: For the web interface



pytesseract: Python wrapper for Tesseract OCR



spacy: For Named Entity Recognition



pillow: For image processing



Install spaCy model: python -m spacy download en_core_web_sm

Notes





The app temporarily saves uploaded images to the uploads/ directory as temp_image.jpg. Ensure this directory exists or create it before running the app.



The Tesseract path in ocr.py is set for Windows. Adjust it for your operating system if needed.

Troubleshooting





Tesseract not found: Ensure Tesseract is installed and the path in ocr.py is correct.



spaCy model not found: Run python -m spacy download en_core_web_sm to download the required model.



Permission issues: Ensure the uploads/ directory has write permissions.

License

This project is licensed under the MIT License.