function getConverted(){
    let inputField = document.getElementById("input");
    let outputField = document.getElementById("output");
    if (inputField.value.length > 0) {
        fetch('/convert', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "text": inputField.value,
                "direction": "latin",
                "type": "modern"
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