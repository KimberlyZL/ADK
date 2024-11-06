function actualizarDoctor(id) {
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const TOficio = document.getElementById('TOficio').value;
    const email = document.getElementById('email').value;
    const contrasenia = document.getElementById('contrasenia').value;
    const codigo = document.getElementById('codigo').value;
    const Institución = document.getElementById('Institución').value;
    const FecNacimiento = document.getElementById('FecNacimiento').value;
    const FecIngreso = document.getElementById('FecIngreso').value;
    const FecRegistro = document.getElementById('FecRegistro').value;

    console.log("Datos a enviar:", { nombre, apellido, TOficio, email, codigo, Institución, FecNacimiento, FecIngreso, FecRegistro });

    fetch(`/actualizar_doctor/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre: nombre,
            apellido: apellido,
            TOficio: TOficio
            email: email,
            contrasenia: contrasenia,
            codigo: codigo,
            Institución: Institución,
            FecNacimiento: FecNacimiento,
            FecIngreso: FecIngreso,
            FecRegistro: FecRegistro,
        })
    })
    .then(response => {
        if (response.ok) {
            alert('Doctor actualizado exitosamente.');
            window.location.href = '/servicio';
        } else {
            alert('Error al actualizar doctor.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}