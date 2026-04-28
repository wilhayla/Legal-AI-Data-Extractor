import pymupdf
from pathlib import Path

def extract_native_text(path_file, output_file):
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

def extract_ocr_text(pdf_file):
    print("PDF detected as scanned. Initializing OCR......")
    
    return None

def extract_text_from_pdf(path_file, output_file):
    pdf_path = Path(path_file)
    print(f"Tryin native extraction to: {pdf_path.name}")

    content = extract_native_text(pdf_path)

    if not content:
        print("Native text not found. Changing to OCR engine.")
        content = extract_ocr_text(pdf_path)
    
    if content:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Succefull peration: Text extracted and save in {output_file}")
        return True
    else:
        print("Error: Failed to extract text using native or OCR methods")
        return False


            

            





