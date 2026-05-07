import re

def clean_extracted_text(text):
    '''This function acts as a noise filter for the extracted text. 
    It removes unwanted characters and formats the text for better readability.'''

    # Pattern to match unwanted characters (e.g., special characters, multiple spaces)
    patterns_to_remove = [
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

    for pattern in patterns_to_remove:
        text = re.sub(pattern, "", text)

    return text