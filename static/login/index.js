document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Login fallido');
        }
    })
    .then(data => {
        console.log(data);
        window.location.href = data.redirect;
    })
    .catch(error => {
        document.getElementById('message').textContent = 'Credenciales incorrectas';
    });
});
