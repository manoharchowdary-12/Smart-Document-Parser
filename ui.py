import streamlit as st
import pdfplumber
import fitz  # PyMuPDF
from PIL import Image
import io

st.title("PDF Text & Image Extractor")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    all_text = ""

    # Extract text using pdfplumber
    with pdfplumber.open(uploaded_file) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                all_text += f"\n--- Page {i+1} ---\n{text}"

    st.text_area("Extracted Text", all_text, height=300)

    # Extract images using PyMuPDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption=f"Page {page_index+1} - Image {img_index+1}")
