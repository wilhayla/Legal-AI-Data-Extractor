import pytest
import pymupdf
from pathlib import Path
from src.extraction import extract_text_from_pdf

# Test 1: verify that the test fails if file is missing
def test_file_not_found():
    result = extract_text_from_pdf("false_file.pdf", "output.txt")
    assert result is False

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
def test_empty_or_short_pdf():
    short_pdf = Path("short_test.pdf")
    output = Path("output_short.txt")

    output.unlink(missing_ok=True)

    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((50,50), "Hello")
    doc.save(short_pdf)
    doc.close()

    result = extract_text_from_pdf(short_pdf, output)

    assert result is True
    assert not output.exists()

    short_pdf.unlink(missing_ok=True)
    output.unlink(missing_ok=True)

def test_corrupt_file():
    corrupt_pdf = Path("corrupt_test.pdf")
    with open(corrupt_pdf, "wb") as f:
        f.write(b"%PDF-1.4\n")
        f.write(b"This is a corrupted file and does not have a real PDF structure.")

    result = extract_text_from_pdf(corrupt_pdf, "output_corrupt.txt")

    assert result is False

    corrupt_pdf.unlink(missing_ok=True)




