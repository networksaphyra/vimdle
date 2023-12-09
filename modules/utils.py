import fitz
import tempfile
import os

def is_pdf_file(filename):
    return filename.lower().endswith(".pdf")

def save_to_temporary_location(pdf_file):
    temp_path = os.path.join(tempfile.gettempdir(), pdf_file.filename)
    pdf_file.save(temp_path)
    return temp_path

def extract_text_from_pdf(pdf_file):
    headings_data = {}
    with fitz.open(pdf_file) as doc:
        for i in range(doc.page_count):
            page = doc[i]
            text = page.get_text("text")
            title = text.split("\n")[0]

            page_data = {
                "content": "".join(text.split("\n")[1:]),
                "title": title
            }
            headings_data[f"Page {i + 1}"] = page_data

    return headings_data 
