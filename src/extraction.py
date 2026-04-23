import pymupdf
from pathlib import Path

def extract_text_from_pdf(path_file, output_file):
    pdf_file = Path(path_file)
    print(f"DEBUG: The file the program is trying to read is: {pdf_file}")

    if not pdf_file.is_file():
        print(f"Error: The file {pdf_file} is not valid.")
        return None
    
    try:
        found_content = False
        with pymupdf.open(pdf_file) as doc:
            text_to_write = [] # and empty list to verify if there are content before to create the output file
            for page in doc:
                raw_text = page.get_text()
                if len(raw_text.strip()) > 10:
                    text_to_write.append(raw_text)
                    found_content = True

        print("Process successfully completed")
        return True
            
    except FileNotFoundError:
        print(f"Error: File not found in {path_file}")
        return False
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
            





