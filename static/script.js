/*
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
*/
function getConverted(){
    let inputField = document.getElementById("input");
    let outputField = document.getElementById("output");
    let typeSelector = document.querySelector("input[name=type-radio]:checked");

    if (inputField.value.length > 0) {
        let type = ""
        if (typeSelector.id == "type-modern") {
            type = "modern"
        } else {
            type = "classic"
        }

        fetch('/convert', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "text": inputField.value,
                "direction": "latin",
                "type": type
            })
        })
        .then(response => response.json())
        .then(response => outputField.value = response["text"])
    } else {
        console.log("The input field was empty. Skipping backend request")
    }
}

function resetInput(){
    let inputField = document.getElementById("input");
    inputField.value = "";
}

function keyEvent(event){
    let modernButton = document.getElementById("type-modern");
    let classicButton = document.getElementById("type-classic");

    if (event.ctrlKey) {
        if (event.key=="Enter") {
            getConverted();
        } else if (event.code == "Digit1") {
            modernButton.checked = true;
        } else if (event.code == "Digit2") {
            classicButton.checked = true;
        } else if (event.code == "Delete") {
            resetInput();
        }
    }
    if (event.code == "F1") {
        showHelp();
    }
}

function showHelp(){
    const helpToast = document.getElementById("helpToast")
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(helpToast)
    toastBootstrap.show()
}

function checkLetters() {
    const alfavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'і', "й",	'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ў', 'ф', 'х', 'ц', 'ч', 'ш', 'ы',  'ь', 'э', 'ю', 'я'];
    const text = document.getElementById("input").value.toLowerCase();
    let notFound = []
    let message = ""


    for (char of alfavit) {
        if  (!text.includes(char)) {
            notFound.push(char)
        }
    }
    if (notFound.length === 0) {
        message = "Усе літары знойдзены"
    } else {
        message = "Няма літар: " + notFound.toString()
    }
    document.getElementById("vyniki").innerHTML = message
    console.log(message);
}