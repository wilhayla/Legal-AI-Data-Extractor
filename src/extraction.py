import pymupdf
from pathlib import Path

def extract_text_from_pdf(path_file, output_file):
    pdf_file = Path(path_file)
    print(f"DEBUG: The file the program is trying to read is: {pdf_file}")

    if not pdf_file.is_file():
        print(f"Error: The file {pdf_file} is not valid.")
        return None
    
    try:
        
            
    
    except FileNotFoundError:
        print(f"Error: File not found in {path_file}")
        return False
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
            





