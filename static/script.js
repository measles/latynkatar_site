function getConverted(){
    var inputField = document.getElementById("input");
    var outputField = document.getElementById("output");
    fetch('/convert', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        "text": inputField.value,
        "operation": "convertation",
        "direction": "latin"
    })
})
    .then(response => response.json())
   //.then(response => console.log(JSON.stringify(response["text"])))
    .then(response => outputField.value = response["text"])
    //document.getElementById("output").value = inputField.value;
}