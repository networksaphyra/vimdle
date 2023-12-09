from ebooklib import epub
from bs4 import BeautifulSoup
import tempfile
import os

def is_epub_file(filename):
    return filename.lower().endswith(".epub")

def save_to_temporary_location(file):
    #FIXME: Returning data is empty, assign it each heading
    temp_path = os.path.join(tempfile.gettempdir(), file.filename)
    file.save(temp_path)
    return temp_path

def extract_headings_from_epub(epub_file):
    headings_data = {}

    book = epub.read_epub(epub_file)

    for i, item in enumerate(book.get_items_of_type(9)):  
        html_content = item.get_body_content().decode('utf-8', errors='ignore')
        soup = BeautifulSoup(html_content, 'html.parser')

        headings = []
        for heading_tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            heading_text = heading_tag.get_text(strip=True)
            headings.append(heading_text)

        headings_data[f"Page {i + 1}"] = headings

    return headings_data