from flask import Flask, render_template, request
import json
from latynkatar import Cyr2Lat

app = Flask(__name__)


@app.route('/')
def index():
    page_suffix = ''
    page_name = "Латынкатар"
    return render_template('index.html', page_name=page_name, page_suffix=page_suffix)


@app.route("/about/")
def about():
    page_name = "Пра сайт"
    page_suffix = f" - {page_name}"
    return render_template('about.html', page_name=page_name, page_suffix=page_suffix)

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    
    converted = Cyr2Lat.convert(data["text"])
    response = {
        "status": "success",
        "text": converted
    }
    response = json.dumps(response)
    
    return response