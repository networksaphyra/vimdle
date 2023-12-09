from flask import Flask, render_template, url_for, jsonify
from modules.config import *
import fitz
import openai

app = Flask(__name__)
openai.api_key = open('.env').readline().strip()

@app.route("/")
def home():
    return render_template("index.html", title="index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    text_data = convert_pdf_to_text(file)
    return jsonify(text_data), 200

def convert_pdf_to_text(pdf_file):
    text_data = {}

    with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text = page.get_text()
            text_data[f"Page {page_number + 1}"] = text

    return text_data

if __name__ == "__main__":
    app.run(debug=True, port=8888)
