// --------------------------------------------------------- //
// Send request from JavaScript, passing information as JSON //
// --------------------------------------------------------- //

const body = document.querySelector('body');
const inputField = document.querySelector('#number');
const enterBtn = document.querySelector('#enter-btn');


// Trigger request when button is clicked
enterBtn.addEventListener('click', myFunction);
function myFunction() {
    // Send request to the route defined in app.py
    fetch('/process', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({number: inputField.value}) // list of key-value pairs to send along with the request
    })
    // Get response
    .then(response => response.json())
    // Actions to perform after the response is received
    .then(data => {
        let newLine = document.createElement('p');
        newLine.innerText = data.output // access content of the response using key set in Flask
        body.appendChild(newLine);
    })
    // Catch possible errors
    .catch(error => console.error('Error:', error));

}