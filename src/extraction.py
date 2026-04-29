import pymupdf
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract

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
    """
    Extract text from scanned PDFs using OCR.
    Requires Poppler(pdf2image) to turn pdf pages into images,
    and pytesseract (the OCR engine that "reads" images.)
    """
    try:
        print("Starting OCR processing (this may take a few seconds).........")

        # 1. Convert PDF pages to images
        # 'dpi=300 is the standard for high-quality OCR
        images = convert_from_path(pdf_file, dpi=300, poppler_path=r'E:\programas\poppler\poppler-25.12.0\Library\bin')

        full_text = [] 

        # Iterate through images and apply OCR
        for i, image in enumerate(images):
            print(f"Processing page {i+1}....")

            # Using 'spa' for Spanish language support
            text = pytesseract.image_to_string(image, lang='spa')
            full_text.append(text)

        return "\n".join(full_text)
    
    except Exception as e:
        print(f"Error during OCR extraction: {e}")
        return None

def extract_text_from_pdf(path_file, output_file):
    """
    Orchestrator function that tries Native extraction first, 
    then falls back to OCR if needed.
    """
    pdf_path = Path(path_file)

    try:
        # 1. Attempt Native Extraction
        print(f"Tryin native extraction to: {pdf_path.name}")
        content = extract_native_text(pdf_path)

        # 2. If not content, attemp OCR.
        if not content:
            print("Native text not found. Changing to OCR engine.")
            content = extract_ocr_text(pdf_path)

        # 3. Final Save
        if content:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Success: Extracted text saved to {output_file}")
            return True
        else:
            print("Error: Failed to extract text using native or OCR methods")
            return False
        
    except Exception as e:
        print(f"An unexpected error occurred while processing the PDF: {e}")
        return False


            

            





