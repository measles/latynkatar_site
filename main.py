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
    return render_template('links.html', page_name=page_name, page_suffix=page_suffix, active_links=ACTIVE, pravapis=links_data.pravapis, knihi=links_data.knihi)


@app.route("/about/")
def about():
    page_name = "Пра сайт"
    page_suffix = f" - {page_name}"
    return render_template('about.html', page_name=page_name, page_suffix=page_suffix, active_about=ACTIVE)

@app.route("/convert", methods=["POST"]) 
@app.route("/convert/", methods=["POST"])
def convert():
    data = request.json
    errors = []
    expected_fields = ("text", "direction", "type")
    
    missed_keys = [ x for x in expected_fields if x not in data.keys() ]
    if missed_keys:
        errors.append(f"Missed required fields: '{', '.join(missed_keys)}'")
        
    unexpected_keys = [ x for x in data.keys() if x not in expected_fields ]
    if unexpected_keys:
        errors.append(f"Unexpected fields: '{', '.join(unexpected_keys)}'")
        
    if "text" in data.keys() and not isinstance(data["text"], str):
        errors.append(f"'text' field should be a String, but was a '{(data['text'].__class__.__name__)}'")
        
    if "direction" in data.keys() and not data["direction"] in ("latin"):
        errors.append(f"'direction' should be 'latin' but was '{data['direction']}'")
        
    if "type" in data.keys() and not data["type"] in ("classic", "modern"):
        errors.append(f"'type' should be either 'classic' or 'modern' but was '{data['type']}'")
        
    if errors:
        response = {
            "status": "error",
            "errors": errors,
        }
    else:
        if data["type"] == "modern":
            converted = Cyr2Lat.convert(data["text"])
        else:
            converted = Cyr2Lat.convert_classic(data["text"])
        response = {
            "status": "success",
            "text": converted,
        }

    response = json.dumps(response)
    
    return response