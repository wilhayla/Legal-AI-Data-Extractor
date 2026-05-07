import pytest
from src.cleaner import clean_extracted_text

def test_remove_camscanner_watermark():
    """Verify that scanning watermarks are successfully filtered out."""
    dirty_text = "Scanned with CamScanner\nLegal Content"
    cleaned = clean_extracted_text(dirty_text)
    assert "Scanned with CamScanner" not in cleaned
    assert "Legal Content" in cleaned

def test_remove_protocol_headers():
    """Verify that administrative and institutional headers are removed."""
    dirty_text = "REPUBLIC OF PARAGUAY\nCOLLEGE OF NOTARIES OF PARAGUAY\nFinca 123"
    cleaned = clean_extracted_text(dirty_text)
    assert "REPUBLIC" not in cleaned
    assert "COLLEGE" not in cleaned
    assert "Finca 123" in cleaned

def test_remove_page_numbers():
    """Verify that automated page numbering is stripped from the text."""
    dirty_text = "Page. 1\nProperty Data\nPage. 2"
    cleaned = clean_extracted_text(dirty_text)
    assert "Page. 1" not in cleaned
    assert "Page. 2" not in cleaned
    assert "Property Data" in cleaned