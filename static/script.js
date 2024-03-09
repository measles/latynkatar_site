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
        console.log

        fetch('/convert', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "text": inputField.value,
                "direction": "latin",
                "type": String(type)
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