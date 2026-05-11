import re

def clean_extracted_text(text):
    '''This function acts as a noise filter for the extracted text. 
    It removes unwanted characters and formats the text for better readability.'''

    # Pattern to match unwanted characters (e.g., special characters, multiple spaces)
    noise_patterns = [

        # 1. Institutional and Notary Specific Text
        r"Colegio de Escribanos.*",
        r"COLEGIO DE ESCRIBANOS DEL PARAGUAY",
        r"REPUBLICA DEL PARAGUAY",
        r"Escaneado con CamScanner",
        r"Registro N\? 78",

        # 2. Contact and Location Information
        r"Chile N\* 902.*",
        r"Fax:.*Asunción.*",
        r"Fax:.*",
        r"Teléfs\.\s.*",

        # 3. Document Identifiers (Series, Sheets, Pages)
        r"Serie .*",
        r"Hoja N° .*",
        r"Pag\. \d+",

        # 4. Structural Regex (Marginal Numbers and Border Noise)
        r"^\d{1,2}\.?\s*$",           # Line numbers (e.g., 1., 2., 18., 24.)
        r"^[A-Z]\s*$",                # Lone letters from border noise
        r"^\s*A\s*$",                 # Variation of lone 'A' noise

        # 5. Security Symbols and Filler Sequences
        r"\.{3,}",                    # Long dot sequences (..........)
        r"={2,}",                     # Sequences of two or more equals signs
        r"={3,}",                     # Sequences of three or more equals signs
        r"_{2,}",                     # Sequences of two or more underscores
        r"_{3,}",                     # Sequences of three or more underscores

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

    # join lines back into a single sanitized string
    return '\n'.join(clean_content)
