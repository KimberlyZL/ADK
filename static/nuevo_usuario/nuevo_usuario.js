const pacienteFields = `
    <div id="pacienteFields">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <br><br>
        
        <label for="apellido">Apellido:</label>
        <input type="text" id="apellido" name="apellido" required>
        <br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>

        <label for="contrasenia">Contraseña:</label>
        <input type="password" id="contrasenia" name="contrasenia" required>
        <br><br>

        <label for="codigo">Código:</label>
        <input type="text" id="codigo" name="codigo" required>
        <br><br>
    </div>
`;

const doctorFields = `
    <div id="doctorFields">
        <label for="nombreDoctor">Nombre:</label>
        <input type="text" id="nombreDoctor" name="nombre" required>
        <br><br>

        <label for="apellidoDoctor">Apellido:</label>
        <input type="text" id="apellidoDoctor" name="apellido" required>
        <br><br>

        <label for="emailDoctor">Email:</label>
        <input type="email" id="emailDoctor" name="email" required>
        <br><br>

        <label for="contraseniaDoctor">Contraseña:</label>
        <input type="password" id="contraseniaDoctor" name="contrasenia" required>
        <br><br>
    </div>
`;

const servicioFields = `
    <div id="servicioFields">
        <label for="emailServicio">Email:</label>
        <input type="email" id="emailServicio" name="email" required>
        <br><br>

        <label for="contraseniaServicio">Contraseña:</label>
        <input type="password" id="contraseniaServicio" name="contrasenia" required>
        <br><br>
    </div>
`;

function updateFields() {
    const rol = document.getElementById('rol').value;
    const camposDiv = document.getElementById('campos');
    camposDiv.innerHTML = '';

    if (rol === 'paciente') {
        camposDiv.innerHTML = pacienteFields;
    } else if (rol === 'doctor') {
        camposDiv.innerHTML = doctorFields;
    } else if (rol === 'servicio') {
        camposDiv.innerHTML = servicioFields;
    }
}

updateFields();

document.getElementById('rol').addEventListener('change', updateFields);

document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const rol = document.getElementById('rol').value;
    let nombre, apellido, email, contrasenia, codigo;

    if (rol === 'paciente') {
        nombre = document.getElementById('nombre').value;
        apellido = document.getElementById('apellido').value;
        email = document.getElementById('email').value;
        contrasenia = document.getElementById('contrasenia').value;
        codigo = document.getElementById('codigo').value;
    } else if (rol === 'doctor') {
        nombre = document.getElementById('nombreDoctor').value;
        apellido = document.getElementById('apellidoDoctor').value;
        email = document.getElementById('emailDoctor').value;
        contrasenia = document.getElementById('contraseniaDoctor').value;
    } else if (rol === 'servicio') {
        email = document.getElementById('emailServicio').value;
        contrasenia = document.getElementById('contraseniaServicio').value;
    }

    fetch('/crear_usuario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rol, nombre, apellido, email, contrasenia, codigo })
    })
    .then(response => {
        if (response.ok) {
            alert('Registro exitoso');
            window.location.href = '/doctor';
        } else {
            alert('Error en el registro');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
