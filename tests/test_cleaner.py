import pytest
from src.cleaner import clean_extracted_text

def test_remove_camscanner_watermark():
    """Verify that scanning watermarks are successfully filtered out."""
    dirty_text = "Escaneado con CamScanner\nLegal Content"
    cleaned = clean_extracted_text(dirty_text)
    assert "Escaneado con CamScanner" not in cleaned
    assert "Legal Content" in cleaned

def test_remove_protocol_headers():
    """Verify that administrative and institutional headers are removed."""
    dirty_text = "REPUBLICA DEL PARAGUAY\nCOLEGIO DE ESCRIBANOS DEL PARAGUAY\nLegal Data"
    cleaned = clean_extracted_text(dirty_text)
    assert "REPUBLICA" not in cleaned
    assert "COLEGIO" not in cleaned
    assert "Legal Data" in cleaned

def test_remove_page_numbers():
    """Verify that automated page numbering is stripped from the text."""
    dirty_text = "Hoja N° 001\nProperty Info\n Pag. 5"
    cleaned = clean_extracted_text(dirty_text)
    assert "Hoja N°" not in cleaned
    assert "Pag." not in cleaned
    assert "Property Info" in cleaned

def test_keep_essential_data():
    """Ensure that critical legal identifiers remain untouched."""
    important_text = "Finca N° 12.580\nCuenta Corriente 14-351-15"
    cleaned = clean_extracted_text(important_text)
    assert cleaned == important_text