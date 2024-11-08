class Manager:
    def __init__(self, db):
        self.db = db

    def obtenerDoctores(self):
        return self.db.obtenerDoctores()

    def obtenerPacientes(self):
        return self.db.obtenerPacientes()
    def obtenerDispensadores(self):
        return self.db.obtenerDispensadores()
    
    def obtenerPaciente(self, id):
        return self.db.obtenerPaciente(id)
    def obtenerDoctor(self, id):
        return self.db.obtenerDoctor(id)
    def obtenerDispensador(self):
        return self.db.obtenerDispensador()

    def login(self, data):
        email = data.get('email')
        password = data.get('password')
        return self.db.login(email, password)

    def crearUsuario(self, data):
        rol = data.get('rol')
        if rol == 'paciente':
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            contrasenia = data.get('contrasenia')
            codigo = data.get('codigo')
            return self.db.insertarPaciente(nombre, apellido, email, contrasenia, codigo)
        elif rol == 'doctor':
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            contrasenia = data.get('contrasenia')
            return self.db.insertarDoctor(nombre, apellido, email, contrasenia)
        elif rol == 'servicio':
            email = data.get('email')
            contrasenia = data.get('contrasenia')
            return self.db.insertarServicio(email, contrasenia)
        return None
    
    def eliminarPaciente(self, id):
        self.db.eliminarPaciente(id)

    def actualizarPaciente(self, data):
        id = data.get('id')
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        contrasenia = data.get('contrasenia')
        codigo = data.get('codigo')
        return self.db.actualizarPaciente(id, nombre, apellido, email, contrasenia, codigo)

    def actualizarDoctor(self, data):
        id = data.get('id')
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        toficio = data.get('toficio')
        email = data.get('email')
        contraseña = data.get('contraseña')
        codigo = data.get('codigo')
        institucion = data.get('institucion')
        fecnacimiento = data.get('fecnacimiento')
        fecregistro = data.get('fecregistro')
        return self.db.actualizarDoctor(id, nombre, apellido, toficio, email, contraseña, codigo, institucion, fecnacimiento, fecregistro)