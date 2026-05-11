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
    
