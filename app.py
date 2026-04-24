import argparse
from pathlib import Path
from src.extraction import extract_text_from_pdf

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

    result = extract_text_from_pdf(input_path, output_path)

    if result is True:
        print(f"Succes! Extracted text saved to: {output_path}")
        print("Error! Extraction fail. Please check the file.")
    else:
        print(f"Error! Input file not found {input_path}")

if __name__ == "__main__":
    main()


