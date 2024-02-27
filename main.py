from flask import Flask, render_template, request
import json
from latynkatar import Cyr2Lat

import lib.links as links_data

ACTIVE = ' active" aria-current="page'

app = Flask(__name__)


@app.route('/')
def index():
    page_suffix = ''
    page_name = "Латынкатар"
    return render_template('index.html', page_name=page_name, page_suffix=page_suffix, active_main=ACTIVE)


@app.route("/links/")
def links():
    page_name = "Спасылкі"
    page_suffix = f" - {page_name}"
    return render_template('links.html', page_name=page_name, page_suffix=page_suffix, active_links=ACTIVE, pravapis=links_data.pravapis)


@app.route("/about/")
def about():
    page_name = "Пра сайт"
    page_suffix = f" - {page_name}"
    return render_template('about.html', page_name=page_name, page_suffix=page_suffix, active_about=ACTIVE)

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