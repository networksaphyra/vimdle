let uploadFileButton = document.getElementById("upload-file-button");
let selectFileButton = document.getElementById("select-file-button");

uploadFileButton.addEventListener("click", function() {
    selectFileButton.click();
    console.log("Clicked the button!")
});

selectFileButton.addEventListener("change", function() {
    const file = selectFileButton.files[0];
    sendDataToBackend(file);
});

function sendDataToBackend(file) {
    console.log("Sent Request...")
    const formData = new FormData();
    formData.append("file", file);

    return fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log("Success:", data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}