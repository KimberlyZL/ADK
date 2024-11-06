import os
from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from db.postgres import DatabasePool
from manager.manager import Manager
from urllib.parse import urlparse


app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key = 'A_SECRET_KEY'

database_url = os.getenv("DATABASE_URL")
url = urlparse(database_url)

db_pool = DatabasePool(
    host=url.hostname,
    port=url.port,
    database=url.path[1:],
    user=url.username,
    password=url.password,
    minconn=1,
    maxconn=20
)

manager = Manager(db_pool)

esp32_current_time = 300000

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('login'))
@app.route('/login', methods=['GET'])
def login():
    return render_template('login/index.html')

@app.route('/login', methods=['POST'])
def registerLogin():
    data = request.json
    response = manager.login(data)

    print(response)
    if response:
        session['email'] = response["email"]
        session['id'] = response["id"]
        session['rol'] = response["rol"]

        if response["rol"] == 'paciente':
            return jsonify({'message': 'Login exitoso', 'redirect': url_for('paginaPaciente')}), 200
        elif response["rol"] == 'doctor':
            return jsonify({'message': 'Login exitoso', 'redirect': url_for('paginaDoctor')}), 200
        elif response["rol"] == 'servicio':
            return jsonify({'message': 'Login exitoso', 'redirect': url_for('paginaServicio')}), 200
    else:
        return jsonify({'message': 'Login fallido'}), 401

@app.route('/paciente')
def paginaPaciente():
    return render_template('paciente/paciente.html')

@app.route('/doctor')
def paginaDoctor():
    pacientes = manager.obtenerPacientes()
    return render_template('doctor/doctor.html', pacientes=pacientes)

@app.route('/servicio')
def paginaServicio():
    return render_template('servicio/servicio.html')

@app.route('/nuevo_usuario')
def nuevoUsuario():
    return render_template('nuevo_usuario/nuevo_usuario.html') 

@app.route('/crear_usuario', methods=['POST'])
def crearUsuario():
    data = request.json
    print(data)
    response = manager.crearUsuario(data)
    if response:
        return jsonify({'message': 'Usuario creado', 'redirect': url_for('paginaDoctor')}), 200
    else:
        return jsonify({'message': 'Creacion de Usuario Fallido'}), 401

@app.route('/editar_paciente/<int:id>', methods=['GET'])
def editarPaciente(id):
    paciente = manager.obtenerPaciente(id)
    return render_template('editar_paciente/editar_paciente.html', paciente=paciente)

@app.route('/actualizar_paciente/<int:id>', methods=['PUT'])
def actualizarPaciente(id):
    data = request.json
    data['id'] = id
    print(data)
    manager.actualizarPaciente(data)
    return jsonify({"message": "Paciente actualizado exitosamente."}), 200

@app.route('/eliminar_paciente/<int:id>', methods=['DELETE'])
def eliminarPaciente(id):
    manager.eliminarPaciente(id)
    return jsonify({'message': 'Paciente eliminado'}), 200

@app.route('/cerrar_sesion')
def cerrarSesion():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/cambiar_tiempo')
def cambiarTiempo():
    return render_template('cambiar_tiempo/cambiar_tiempo.html')

@app.route('/editardoctor')
def editardoctor():
    return render_template('editar_doctor/editar_doctor.html')

@app.route('/form_doctor')
def formdoctor():
    doctores = manager.obtener_doctores()
    print (doctores)
    return render_template('form_doctor/form_doctor.html', doctores=doctores)


@app.route('/esp32_time', methods=['GET'])
def esp32_time():
    global esp32_current_time
    print(f"Return Time to ESP32: {esp32_current_time}")
    return jsonify({"data": esp32_current_time})


@app.route('/send', methods=['POST'])
def send_data():
    global esp32_current_time
    data = request.get_json().get('data')

    if data is not None:
        esp32_current_time = int(data)
        print(f"Tiempo actualizado por ESP32: {esp32_current_time}")
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "No se recibió ningún dato"}), 400


if __name__ == '__main__':
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 5000))
    #app.run(debug=True)
    app.run(debug=True, host=host, port=port)