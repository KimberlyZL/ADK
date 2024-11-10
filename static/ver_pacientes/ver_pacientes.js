function eliminarPaciente(id) {
    if (confirm('¿Estás seguro de que deseas eliminar este paciente?')) {
        fetch(`/eliminar_paciente/${id}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                alert('Paciente eliminado exitosamente');
                location.reload();
            } else {
                alert('Error al eliminar el paciente');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al eliminar el paciente');
        });
    }
}

function filtrarPorApellido() {
    const filtro = document.getElementById('filterApellido').value.toLowerCase();
    const filas = document.querySelectorAll('#tablaPacientes tr');

    filas.forEach(fila => {
        const apellido = fila.querySelector('td[data-th="Apellido"]');
        if (apellido) {
            const textoApellido = apellido.textContent.toLowerCase();
            fila.style.display = textoApellido.includes(filtro) ? '' : 'none';
        }
    });
}