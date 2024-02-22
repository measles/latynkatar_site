from flask import Flask, render_template, request
import json
from latynkatar import Cyr2Lat

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    
    converted = Cyr2Lat.convert(data["text"])
    response = {
        "status": "success",
        "text": converted
    }
    responce = json.dumps(response)
    
    return response