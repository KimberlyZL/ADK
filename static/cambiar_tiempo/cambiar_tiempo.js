document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const hours = document.getElementById('hoursInput').value;
    const minutes = document.getElementById('minutesInput').value;

    const millis = (hours * 3600000) + (minutes * 60000);

    fetch('/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: millis })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/servicio';
        } else {
            alert("Error al enviar el formulario");
        }
    })
    .catch(error => {
        console.error('Error al enviar el dato:', error);
    });
});
