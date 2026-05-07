import re

def clean_extracted_text(text):
    '''This function acts as a noise filter for the extracted text. 
    It removes unwanted characters and formats the text for better readability.'''

    # Pattern to match unwanted characters (e.g., special characters, multiple spaces)
    noise_patterns = [
        r"Escaneado con CamScanner",
        r"COLEGIO DE ESCRIBANOS DEL PARAGUAY",
        r"REPUBLICA DEL PARAGUAY",
        r"Serie .*",           # Matches "Serie " followed by any characters
        r"Hoja N° .*",         # Matches "Hoja N° " followed by any characters
        r" Pag\. \d+",         # Matches " Pag. " followed by one or more digits
        r"={3,}",              # Matches sequences of three or more equal signs
        r"_{3,}",              # Matches sequences of three or more underscores

    ]

    # Split into lines for granular processing
    lines = text.split('\n')
    clean_content = []

    for line in lines:
        clean_line = line.strip()  # Remove leading and trailing whitespace

        # Skip empty strings
        if not clean_line:
            continue

        # Validate line against noise blacklist
        is_metadata_noise = any(re.search(p, clean_line, re.IGNORECASE) for p in noise_patterns)

        if not is_metadata_noise:
            clean_content.append(clean_line)
        