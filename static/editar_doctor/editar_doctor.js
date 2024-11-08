function actualizarDoctor(id) {
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const toficio = document.getElementById('toficio').value;
    const email = document.getElementById('email').value;
    const contraseña = document.getElementById('contraseña').value;
    const codigo = document.getElementById('codigo').value;
    const institucion = document.getElementById('institucion').value;
    const fecnacimiento = document.getElementById('fecnacimiento').value;
    const fecregistro = document.getElementById('fecregistro').value;

    console.log("Datos a enviar:", { nombre, apellido, toficio, email, contraseña, codigo, institucion, fecnacimiento, fecregistro });

    fetch(`/actualizar_doctor/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre: nombre,
            apellido: apellido,
            toficio:toficio
            email: email,
            contraseña: contraseña,
            codigo: codigo,
            institucion: institucion,
            fecnacimiento: fecnacimiento,
            fecregistro: fecregistro,
        })
    })
    .then(response => {
        if (response.ok) {
            alert('Doctor actualizado exitosamente.');
            window.location.href = '/form_doctor';
        } else {
            alert('Error al actualizar el doctor.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
