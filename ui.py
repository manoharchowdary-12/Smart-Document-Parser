import streamlit as st
import os
import sys

# Import modules
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from app.ocr import extract_text_from_image, extract_text_from_pdf, summarize_text
from app.ner import extract_entities

# Streamlit app config
st.set_page_config(page_title="Smart Document Parser", layout="wide")
st.title("📄 Smart Document Parser (OCR + NER + Summarization)")

# File uploader: images + PDFs
uploaded_file = st.file_uploader("Upload a document", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    temp_file_path = os.path.join(os.getcwd(), f"temp_file.{file_extension}")

    # Save uploaded file
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text depending on type
    if file_extension in ["png", "jpg", "jpeg"]:
        st.image(temp_file_path, caption="Uploaded Image", use_column_width=True)
        text = extract_text_from_image(temp_file_path)
    else:  # PDF
        text = extract_text_from_pdf(temp_file_path)

    # Show extracted text
    st.subheader("📑 Extracted Text")
    st.text_area("Full Text", text, height=300)

    # Show summary
    st.subheader("📝 Summary")
    summary = summarize_text(text)
    st.text_area("Summary", summary, height=200)

    # Named Entity Recognition
    st.subheader("🔍 Named Entities")
    entities = extract_entities(text)
    if entities:
        st.table(entities)
    else:
        st.write("No entities found.")