import pytest
import pymupdf
from pathlib import Path
from src.extraction import extract_text_from_pdf

# Test 1: verify that the test fails if file is missing
def test_file_not_found():
    result = extract_text_from_pdf("false_file.pdf", "output.txt")
    assert result is None

# Test 2: Verify behavior with a real file
def test_succeful_extraction():
    pdf_input = Path("data/inputs/title_deed.pdf")
    output = Path("data/outputs/output_test.txt")

    if pdf_input.exists():
        result = extract_text_from_pdf(pdf_input, output)
        assert result is True

        if output.exists():
            output.unlink()
    else:
        pytest.skip("Test file not found, skipping test.")

# Test 3: Testing an empty page or with short characters.
def test_emty_or_short_pdf():
    short_pdf = Path("short_test.pdf")
    output = Path("output_short.txt")

    doc = pymupdf.open()
    page = doc.new_page()



