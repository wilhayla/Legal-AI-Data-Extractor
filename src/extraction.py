import pymupdf
from pathlib import Path

def extract_text_from_pdf():
    pdf_file = Path("title_deed.pdf")
    print(f"DEBUG: The file the program is trying to read is: {pdf_file}")

    if not pdf_file.is_file():
        print(f"Error: The file {pdf_file} is not valid.")
        return None


extract_text_from_pdf()

