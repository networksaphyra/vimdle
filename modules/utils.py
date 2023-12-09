import fitz

def convert_pdf_to_text(pdf_file):
    text_data = {}

    with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text = page.get_text()
            text_data[f"Page {page_number + 1}"] = text

    return text_data
