import pytest
from pathlib import Path
from src.extraction import extract_text_from_pdf

# Test 1: verify that the test fails if file is missing
def test_file_not_found():
    result = extract_text_from_pdf("false_file.pdf", "output.txt")
    assert result is None

