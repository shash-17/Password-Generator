function generatePassword() {
    let length = document.getElementById("length").value;

    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ length: length })
    })
    .then(response => response.json())
    .then(data => {
        if (data.password) {
            document.getElementById("password").value = data.password;
            document.getElementById("message").innerText = "";
        } else {
            document.getElementById("message").innerText = data.error;
        }
    })
    .catch(error => console.error('Error:', error));
}

function copyToClipboard() {
    let passwordField = document.getElementById("password");
    passwordField.select();
    document.execCommand("copy");
    document.getElementById("message").innerText = "Copied to clipboard!";
}
