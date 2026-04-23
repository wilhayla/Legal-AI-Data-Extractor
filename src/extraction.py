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
            for page in doc:
                raw_text = page.get_text()

                if len(raw_text.strip()) > 10:
                    text_bytes = raw_text.encode("utf8")
                    out.write(text_bytes)
                    out.write(bytes((12,)))
                else:
                    print("Page skipped: content is too short.")

        print("Process successfully completed")
        return True
            
    except FileNotFoundError:
        print(f"Error: File not found in {path_file}")
        return False
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
            





