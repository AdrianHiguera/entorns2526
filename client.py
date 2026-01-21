import requests

# Modelo Usuario
class User:
    def __init__(self, username, nom, email, rol="tutor"):
        self.username = username
        self.nom = nom
        self.email = email
        self.rol = rol
    
    def __str__(self):
        return f"{self.nom} ({self.rol}) - {self.email}"

# DAO cliente
class daoUserClient: 
    def __init__(self, server_url="http://127.0.0.1:5000"):
        self.server_url = server_url

    def getUserByUsername(self, username):
        try:
            response = requests.get(f"{self.server_url}/user", params={"username": username})
            if response.status_code == 200:
                data = response.json()
                if "msg" in data:
                    return data
                # Convertimos el JSON a objeto User
                return User(
                    username=data["username"],
                    nom=data["nom"],
                    email=data["email"],
                    rol=data["rol"]
                )
            else:
                return {"msg": "Error en la petició"}
        except Exception as e:
            return {"msg": f"Error de connexió: {e}"}

# Vista en consola
class ViewConsole:
    def getInputUsername(self):
        return input("Introdueix el username: ")

    def showUserInfo(self, user_data):
        if isinstance(user_data, dict) and "msg" in user_data:
            print(user_data["msg"])
        else:
            print("Usuari trobat:")
            print(user_data)


daoUserClient = daoUserClient()
u=daoUserClient.getUserByUsername("rob")
print(u)
u=daoUserClient.getUserByUsername("NOTexists")
print(u)