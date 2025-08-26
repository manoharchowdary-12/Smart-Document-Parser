import spacy

# Try to load model, download if missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    """Extract named entities from input text."""
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
