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
