from flask import Flask, jsonify, request

app = Flask(__name__)


class User:
    def __init__(self,username, nom, password, email, rol="tutor"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom

class Child:
    def __init__(self,name, age, parent_username):
        self.name=name
        self.age=age
        self.parent_username=parent_username
    
    def to_dict(self):
        return {"name": self.name, "age": self.age, "parent": self.parent_username}


users = [
    User(username="rob",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor"),
    User(username="john",nom="John Cannigan",password="12345", email="john@gmail.com",rol="tutor"),
    User(username="maria",nom="Maria Sams",password="12345", email="maria@gmail.com",rol="admin")
]

children = [
    Child("Pedro", 5, "rob"),
    Child("Ana", 7, "rob"),
    Child("Luis", 6, "john")
]


class UserDao:
    def __init__(self):
        self.users=users
    
    def getUserByUsername(self,uname):
        for u in self.users:
            if u.username == uname:
                return u.__dict__
        return None

    def getAllUsers(self):
        return [u.__dict__ for u in self.users]


class ChildDao:
    def __init__(self):
        self.children = children
    
    def getChildrenByUsername(self, username):
        return [c.to_dict() for c in self.children if c.parent_username == username]
    
    def getAllChildren(self):
        return [c.to_dict() for c in self.children]


user_dao = UserDao()
child_dao = ChildDao()


@app.route('/user', methods=['GET'])
def user():
    username = request.args.get("username", default="")
    if username:
        u = user_dao.getUserByUsername(username)
        if u:
            return jsonify(u)
        return jsonify({"msg":"Usuario no encontrado"}), 404
    return jsonify({"msg":"Falta parámetro username"}), 400

@app.route('/getusers', methods=['GET'])
def all_users():
    return jsonify(user_dao.getAllUsers())


@app.route('/children', methods=['GET'])
def children_by_user():
    username = request.args.get("username", default="")
    if username:
        children_list = child_dao.getChildrenByUsername(username)
        return jsonify(children_list)
    return jsonify({"msg":"Falta parámetro username"}), 400

@app.route('/allchildren', methods=['GET'])
def all_children():
    return jsonify(child_dao.getAllChildren())

if __name__ == '__main__':
    app.run(debug=True)