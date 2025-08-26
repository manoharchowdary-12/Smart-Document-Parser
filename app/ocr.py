import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import pdfplumber
from transformers import pipeline

# Tesseract path (update if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Use smaller, faster summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_image(image_path: str) -> str:
    """Extract text from an image file using OCR."""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF (handles both digital text and scanned images)."""
    full_text = ""

    # Try direct text extraction with pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text and text.strip():
                # Direct text exists
                full_text += f"\n--- Page {page_num} (text) ---\n{text}\n"
            else:
                # Fallback to OCR for scanned pages
                poppler_path = r"C:\Users\manuc\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin"
                image_pages = convert_from_path(
                    pdf_path, first_page=page_num, last_page=page_num, poppler_path=poppler_path
                )
                for img in image_pages:
                    text = pytesseract.image_to_string(img)
                    full_text += f"\n--- Page {page_num} (OCR) ---\n{text}\n"

    return full_text

def summarize_text(text: str, max_words: int = 150) -> str:
    """Summarize long text into a concise form."""
    if not text or len(text.split()) < 50:
        return "Text too short for summarization."
    summary = summarizer(text, max_length=max_words, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    # Example runs
    img_text = extract_text_from_image("sample.png")
    print("Extracted text from image:\n", img_text)
    print("Summary:\n", summarize_text(img_text))

    pdf_text = extract_text_from_pdf("sample.pdf")
    print("Extracted text from PDF:\n", pdf_text)
    print("Summary:\n", summarize_text(pdf_text))