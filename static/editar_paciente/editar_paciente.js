function actualizarPaciente(id) {
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const email = document.getElementById('email').value;
    const contrasenia = document.getElementById('contrasenia').value;
    const codigo = document.getElementById('codigo').value;

    fetch(`/actualizar_paciente/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre: nombre,
            apellido: apellido,
            email: email,
            contrasenia: contrasenia,
            codigo: codigo
        })
    })
    .then(response => {
        if (response.ok) {
            alert('Paciente actualizado exitosamente.');
            window.location.href = '/doctor';
        } else {
            alert('Error al actualizar el paciente.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
