import argparse
from pathlib import Path
from src.extraction import extract_text_from_pdf
from src.cleaner import clean_extracted_text

def main():
    parser = argparse.ArgumentParser(description="Legal-AI-Data_Extractor: Tool to extract text from legal PDF file")

    # Define the arguments the user must enter
    parser.add_argument("input_pdf", type=str, help="Input PDF file path")
    parser.add_argument("output_txt", type=str, help="Output TXT file path")

    args = parser.parse_args() # code that validate data and save it as an object to args variable

    input_path = Path(args.input_pdf)
    output_path = Path(args.output_txt)

    print(f"---Start extraction---")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    raw_text = extract_text_from_pdf(input_path, output_path)

    if raw_text is True:
        print(f"Succes! Extracted text saved to: {output_path}")
        print(f"DEBUG: The file is saving at: {output_path.absolute()}")
        
        # Read the extracted text from the file for cleaning
        with open(output_path, "r", encoding="utf-8") as f:
            extracted_content = f.read()
        
        # Cleaning (Integration)
        # inmmediately after extraction, we pass that text through the cleaner utility
        cleaned_text = clean_extracted_text(extracted_content)
    elif raw_text is False:
        print("Error! Extraction fail. Please check the file.")
        return
    else:
        print(f"Error! Input file not found {input_path}")
        return

    # 3. Final save
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    
    print("Process complete: Extraction and Cleaning finalized!")

    

if __name__ == "__main__":
    main()


