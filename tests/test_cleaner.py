import pytest
from src.cleaner import clean_extracted_text

def test_remove_camscanner_watermark():
    """Verify that scanning watermarks are successfully filtered out."""
    dirty_text = "Scanned with CamScanner\nLegal Content"
    cleaned = clean_extracted_text(dirty_text)
    assert "Scanned with CamScanner" not in cleaned
    assert "Legal Content" in cleaned