from flask import Flask, render_template, url_for, request, jsonify
from modules.config import *
import modules.utils as utils
import openai

app = Flask(__name__)
openai.api_key = open('.env').readline().strip()

@app.route("/")
def home():
    return render_template("index.html", title="index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    text_data = utils.convert_pdf_to_text(file)
    print(text_data)
    return jsonify(text_data), 200


if __name__ == "__main__":
    app.run(debug=True, port=8888)
