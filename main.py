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

from flask import Flask, render_template, request
import json
import latynkatar

from lib.links import RAZDZIEŁY

app = Flask(__name__)


@app.route("/")
def index():
    page_suffix = ""
    page_name = "Латынкатар"
    return render_template("index.j2", page_name=page_name, page_suffix=page_suffix, debug=app.config["DEBUG"])


@app.route("/links/")
def links():
    page_name = "Спасылкі"
    page_suffix = f" - {page_name}"
    return render_template(
        "links.j2", page_name=page_name, page_suffix=page_suffix, spasylki=RAZDZIEŁY, debug=app.config["DEBUG"]
    )


@app.route("/about/")
def about():
    page_name = "Пра сайт"
    page_suffix = f" - {page_name}"
    return render_template("about.j2", page_name=page_name, page_suffix=page_suffix, debug=app.config["DEBUG"])


@app.route("/litary/")
def litary():
    page_name = "Усе літары"
    page_suffix = f" - {page_name}"
    return render_template("litary.j2", page_name=page_name, page_suffix=page_suffix, debug=app.config["DEBUG"])


@app.route("/convert", methods=["POST"])
@app.route("/convert/", methods=["POST"])
def convert():
    data = request.json
    errors = []
    expected_fields = ("text", "direction", "type", "palatalization")

    missed_keys = [x for x in expected_fields if x not in data.keys()]
    if missed_keys:
        errors.append(f"Missed required fields: '{', '.join(missed_keys)}'")

    unexpected_keys = [x for x in data.keys() if x not in expected_fields]
    if unexpected_keys:
        errors.append(f"Unexpected fields: '{', '.join(unexpected_keys)}'")

    if "text" in data.keys() and not isinstance(data["text"], str):
        errors.append(
            f"'text' field should be a String, but was a '{(data['text'].__class__.__name__)}'"
        )

    if "direction" in data.keys() and not data["direction"] in ("latin"):
        errors.append(f"'direction' should be 'latin' but was '{data['direction']}'")

    if "type" in data.keys() and not data["type"] in ("old", "modern"):
        errors.append(
            f"'type' should be either 'old' or 'modern' but was '{data['type']}'"
        )

    if errors:
        response = {
            "status": "error",
            "errors": errors,
        }
    else:
        if data["type"] == "modern":
            converted = latynkatar.convert(
                data["text"], miakkasc=data["palatalization"]
            )
        else:
            converted = latynkatar.convert_old(
                data["text"], miakkasc=data["palatalization"]
            )
        response = {
            "status": "success",
            "text": converted,
        }

    response = json.dumps(response)

    return response
