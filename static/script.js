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
        } else if (event.code = "Delete") {
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
