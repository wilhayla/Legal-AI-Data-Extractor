import argparse
from pathlib import Path
from src.extraction import extract_text_from_pdf

def main():
    parser = argparse.ArgumentParser(description="Legal-AI-Data_Extractor: Tool to extract text from legal PDF file")

    # Define the arguments the user must enter
    parser.add_argument("input_pdf", type=str, help="Input PDF file path")
    parser.add_argument("output_txt", type=str, help="Output TXT file path")

    args = parser.parse_args() # code that validate data and save it as an object to args variable