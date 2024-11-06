import psycopg2
from psycopg2 import pool

class DatabasePool:
    def __init__(self, host, port, database, user, password, minconn=1, maxconn=20):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.minconn = minconn
        self.maxconn = maxconn
        self.connectionPool = None
        self.initializePool()

    def initializePool(self):
        try:
            self.connectionPool = psycopg2.pool.SimpleConnectionPool(
                self.minconn,
                self.maxconn,
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connection pool initialized")
        except Exception as e:
            print(f"Error initializing pool: {e}")

    def getConnection(self):
        try:
            connection = self.connectionPool.getconn()
            if connection:
                print("Connection acquired from pool")
                return connection
        except Exception as e:
            print(f"Error getting connection from pool: {e}")

    def releaseConnection(self, connection):
        try:
            self.connectionPool.putconn(connection)
            print("Connection returned to pool")
        except Exception as e:
            print(f"Error releasing connection to pool: {e}")

    def closeAllConnections(self):
        try:
            if self.connectionPool:
                self.connectionPool.closeall()
                print("All pool connections closed")
        except Exception as e:
            print(f"Error closing all pool connections: {e}")

    def executeQuery(self, query, params=None):
        connection = self.getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
            print("Query executed successfully")
            return cursor.rowcount
        except Exception as e:
            print(f"Error executing query: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            self.releaseConnection(connection)

    def fetchQuery(self, query, params=None):
        connection = self.getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            cursor.close()
            self.releaseConnection(connection)

    def obtenerPacientes(self):
        query = "SELECT * FROM paciente"
        return self.fetchQuery(query)
    def obtener_doctores(self):
        query = "SELECT * FROM Doctor"
        return self.fetchQuery(query)
    def obtenerPaciente(self, id):
        queryPaciente = """
        SELECT id, nombre, apellido, email, contrasenia, codigo, 'paciente' AS rol 
        FROM paciente 
        WHERE id = %s
        """
        pacienteResult = self.fetchQuery(queryPaciente, (id,))
        if pacienteResult:
            return {
                'id': pacienteResult[0][0],
                'nombre': pacienteResult[0][1],
                'apellido': pacienteResult[0][2],
                'email': pacienteResult[0][3],
                'contrasenia': pacienteResult[0][4],
                'codigo': pacienteResult[0][5],
                'rol': 'paciente'
            }
        return None


    def insertarPaciente(self, nombre, apellido, email, contrasenia, codigo):
        query = """
        INSERT INTO paciente (nombre, apellido, email, contrasenia, codigo)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
        """
        params = (nombre, apellido, email, contrasenia, codigo)
        connection = self.getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            new_id = cursor.fetchone()[0]
            connection.commit()
            print("New patient inserted successfully with ID:", new_id)
            return new_id
        except Exception as e:
            print(f"Error inserting patient: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            self.releaseConnection(connection)

    def insertarDoctor(self, nombre, apellido, email, contrasenia):
        query = """
        INSERT INTO doctor (nombre, apellido, email, contrasenia)
        VALUES (%s, %s, %s, %s) RETURNING id
        """
        params = (nombre, apellido, email, contrasenia)
        connection = self.getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            new_id = cursor.fetchone()[0]
            connection.commit()
            print("New patient inserted successfully with ID:", new_id)
            return new_id
        except Exception as e:
            print(f"Error inserting patient: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            self.releaseConnection(connection)

    def insertarServicio(self, email, contrasenia):
        query = """
        INSERT INTO servicio (email, contrasenia)
        VALUES (%s, %s) RETURNING id
        """
        params = (email, contrasenia)
        connection = self.getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            new_id = cursor.fetchone()[0]
            connection.commit()
            print("New patient inserted successfully with ID:", new_id)
            return new_id
        except Exception as e:
            print(f"Error inserting patient: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            self.releaseConnection(connection)

    def actualizarPaciente(self, paciente_id, nombre=None, apellido=None, email=None, contrasenia=None, codigo=None):
        query = "UPDATE paciente SET "
        fields = []
        params = []
        if nombre:
            fields.append("nombre = %s")
            params.append(nombre)
        if apellido:
            fields.append("apellido = %s")
            params.append(apellido)
        if email:
            fields.append("email = %s")
            params.append(email)
        if contrasenia:
            fields.append("contrasenia = %s")
            params.append(contrasenia)
        if codigo:
            fields.append("codigo = %s")
            params.append(codigo)

        query += ", ".join(fields) + " WHERE id = %s"
        params.append(paciente_id)
        return self.executeQuery(query, tuple(params))

    def eliminarPaciente(self, paciente_id):
        query = "DELETE FROM paciente WHERE id = %s"
        params = (paciente_id,)
        return self.executeQuery(query, params)

    def login(self, email, password):
        queryPaciente = """
        SELECT id, nombre, apellido, email, 'paciente' AS rol 
        FROM paciente 
        WHERE email = %s AND contrasenia = %s
        """
        queryDoctor = """
        SELECT id, nombre, apellido, email, 'doctor' AS rol 
        FROM doctor 
        WHERE email = %s AND contrasenia = %s
        """
        queryServicio = """
        SELECT id, email, 'servicio' AS rol 
        FROM servicio 
        WHERE email = %s AND contrasenia = %s
        """

        pacienteResult = self.fetchQuery(queryPaciente, (email, password))
        if pacienteResult:
            return {
                'id': pacienteResult[0][0],
                'nombre': pacienteResult[0][1],
                'apellido': pacienteResult[0][2],
                'email': pacienteResult[0][3],
                'rol': 'paciente'
            }

        doctorResult = self.fetchQuery(queryDoctor, (email, password))
        if doctorResult:
            return {
                'id': doctorResult[0][0],
                'nombre': doctorResult[0][1],
                'apellido': doctorResult[0][2],
                'email': doctorResult[0][3],
                'rol': 'doctor'
            }

        servicioResult = self.fetchQuery(queryServicio, (email, password))
        if servicioResult:
            return {
                'id': servicioResult[0][0],
                'email': servicioResult[0][1],
                'rol': 'servicio'
            }

        return None