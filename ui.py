import streamlit as st
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from app.ocr import extract_text
from app.ner import extract_entities

st.set_page_config(page_title="Smart Document Parser", layout="wide")
st.title("📄 Smart Document Parser (OCR + NER)")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    temp_file_path = os.path.join(os.getcwd(), "temp_image.jpg")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(temp_file_path, caption="Uploaded Image", use_column_width=True)

    text = extract_text(temp_file_path)
    st.subheader("Extracted Text")
    st.text_area("", text, height=200)

    entities = extract_entities(text)
    st.subheader("Named Entities")
    if entities:
        st.table(entities)
    else:
        st.write("No entities found.")
