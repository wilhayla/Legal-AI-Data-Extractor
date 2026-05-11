from src.cleaner import clean_extracted_text
from pathlib import Path

def process_document(imput_path: Path, output_path: Path):
    '''
    Orchestrates the cleaning procees of extracted legal text using path objects
    '''
    # 1. Validate imput file existance
    if not imput_path.exists():
        print(f"Error: Target file not found {imput_path}.")
        return
    
    # 2. Read the raw text from the input file
    raw_text = imput_path.read_text(encoding='utf-8')

    # 3. Apply the cleaning logic.
    cleaned_text = clean_extracted_text(raw_text)

    # 4. Save the cleaned text to the output file
    output_path.write_text(cleaned_text, encoding='utf-8')

    print(f"Successfully processed cleaned text at: {output_path}.")

    
