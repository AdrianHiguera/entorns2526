from flask import Flask, jsonify, request

# Modelo Usuario
class User:
    def __init__(self, username, nom, password, email, rol="tutor"):
        self.username = username
        self.nom = nom
        self.password = password
        self.email = email
        self.rol = rol
    
    def to_dict(self):
        """Devuelve solo los datos públicos (sin password)"""
        return {
            "username": self.username,
            "nom": self.nom,
            "email": self.email,
            "rol": self.rol
        }

# Lista de usuarios
users = [
    User(username="rob", nom="Rob Halford", password="12345", email="rob@gmail.com", rol="tutor"),
    User(username="john", nom="John Cannigan", password="12345", email="john@gmail.com", rol="tutor"),
    User(username="maria", nom="Maria Sams", password="12345", email="maria@gmail.com", rol="admin")
]

# DAO de usuarios
class UserDao:
    def __init__(self):
        self.users = users

    def getUserByUsername(self, uname):
        for u in self.users:
            if u.username == uname:
                return u.to_dict()
        return None

    def getAllUsers(self):
        return [u.to_dict() for u in self.users]

# Instancia del DAO
user_dao = UserDao()

# Flask app
app = Flask(__name__)

# Endpoint para buscar un usuario por username
@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get("username", default="")
    if not username:
        return jsonify({"msg": "Falta paràmetre Username"})
    
    user_data = user_dao.getUserByUsername(username)
    if not user_data:
        return jsonify({"msg": "Usuari no trobat"})
    
    return jsonify(user_data)

# Endpoint para listar todos los usuarios
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(user_dao.getAllUsers())

# Bloque principal para Windows
if __name__ == '__main__':
    # host=127.0.0.1 asegura que solo sea accesible localmente
    # port=5000 es el puerto por defecto
    app.run(debug=True, host="127.0.0.1", port=5000)
