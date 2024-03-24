"""
BSD 3-Clause License

Copyright (c) 2024, Andrej Zacharevicz

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pydoc import pager
from flask import Flask, render_template, request
from flask_babel import Babel, lazy_gettext
import json
from latynkatar import Cyr2Lat
from config import Config

import lib.links as links_data

ACTIVE = ' active" aria-current="page'


def get_locale():
    print(app.config)
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    data = {
        "page_name": lazy_gettext("Латынкатар"),
        "page_suffix": '',
        "page": "main",
    }
    return render_template('index.html', data=data)


@app.route("/links/")
def links():
    page_name = lazy_gettext("Спасылкі")
    data = {
        "page_name": page_name,
        "page_suffix": f" - {page_name}",
        "page": "links",
        "pravapis": links_data.pravapis,
        "knihi": links_data.pravapis,
    }
    return render_template('links.html', data=data)


@app.route("/about/")
def about():
    page_name = lazy_gettext("Пра сайт")
    data = {
        "page_name": page_name,
        "page_suffix": f" - {page_name}",
        "page": "about",
    }
    return render_template('about.html', data=data)

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
