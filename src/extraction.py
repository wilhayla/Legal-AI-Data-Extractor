import pymupdf
from pathlib import Path

def extract_text_from_pdf(path_file, output_file):
    pdf_file = Path(path_file)
    print(f"DEBUG: The file the program is trying to read is: {pdf_file}")

    if not pdf_file.is_file():
        print(f"Error: The file {pdf_file} is not valid.")
        return None
    
    text_list = [] 
    with pymupdf.open(pdf_file) as doc:
        for page in doc:
            raw_text = page.get_text()
            if len(raw_text.strip()) > 10:
                text_list.append(raw_text)

        if text_list:
            return "\n".join(text_list)
            

            





