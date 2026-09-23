from app.pdf_parser import extract_text_from_pdf


def test_extract_text_from_pdf():

    file_path = "data/pdfs/business_report.pdf"

    text = extract_text_from_pdf(file_path)

    assert "Business Performance Report" in text
    assert "Amit" in text
    assert "Department: IT" in text
    assert "90%" in text
    assert "Neha" in text