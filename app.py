from flask import Flask, render_template, url_for, request, jsonify
from modules.config import *
import modules.utils as utils
import os
import openai

app = Flask(__name__)
openai.api_key = open('.env').readline().strip()

@app.route("/")
def home():
    return render_template("index.html", title="index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if not utils.is_epub_file(file.filename):
        return jsonify({"error": "Invalid File Format"}), 400
        
    temp_path = utils.save_to_temporary_location(file)
    text_data = utils.extract_headings_from_epub(temp_path)
    print(text_data)

    os.remove(temp_path)
    return jsonify(text_data), 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
