from flask import Flask, request, jsonify
from DaoServer import UserDAO, ChildDAO
from dadesServer import User

app = Flask(__name__)

userDao = UserDAO()
childDao = ChildDAO()

# -----------------------------
# LOGIN
# -----------------------------
@app.route('/login', methods=['POST'])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    user = userDao.login(username, password)

    if user:
        return jsonify({
            "coderesponse": "1",
            "msg": "Authenticated",
            "data": user
        }), 200

    return jsonify({
        "coderesponse": "0",
        "msg": "No validat"
    }), 400


# -----------------------------
# CHILD SERVICE
# -----------------------------
@app.route('/child', methods=['POST'])
def getChildren():

    token = request.headers.get("Authorization")

    if not token:
        return jsonify({
            "coderesponse": "0",
            "msg": "Token missing"
        }), 400

    data = request.json
    iduser = data.get("iduser")

    user = User(iduser, "", "", "", 1, token)

    childs = childDao.getChilds(user)

    return jsonify({
        "coderesponse": "1",
        "msg": str(len(childs)),
        "data": childs
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def home():
    return "Server running"