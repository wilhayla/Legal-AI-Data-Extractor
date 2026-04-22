import pymupdf
from pathlib import Path

def extract_text_from_pdf():
    pdf_file = Path("title_deed.pdf")
    print(f"DEBUG: The file the program is trying to read is: {pdf_file}")

extract_text_from_pdf()

