from flask import Flask, jsonify, request

app = Flask(__name__)


class Child:
    def __init__(self, name, age, parent_username):
        self.name = name
        self.age = age
        self.parent_username = parent_username
    
    def to_dict(self):
        return {"name": self.name, "age": self.age, "parent": self.parent_username}


children = [
    Child("Messi", 5, "rob"),
    Child("Sergio", 7, "rob"),
    Child("Diana", 6, "john"),
    Child("Sheila", 8, "maria")
]

class ChildDao:
    def __init__(self):
        self.children = children
    
    def getChildrenByUsername(self, username):
        # Devuelve solo los hijos del usuario
        return [c.to_dict() for c in self.children if c.parent_username == username]
    
    def getAllChildren(self):
        # Devuelve todos los hijos
        return [c.to_dict() for c in self.children]


child_dao = ChildDao()

@app.route('/children', methods=['GET'])
def children_by_user():
    username = request.args.get("username", default="")
    if username:
        children_list = child_dao.getChildrenByUsername(username)
        return jsonify(children_list)
    return jsonify({"msg": "Falta parámetro username"}), 400

@app.route('/allchildren', methods=['GET'])
def all_children():
    return jsonify(child_dao.getAllChildren())

if __name__ == '__main__':
    app.run(debug=True)
