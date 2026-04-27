
from dataclasses import asdict, dataclass

from flask import Flask, jsonify, request

app = Flask(__name__)

from DaoServer import ChildDAO, UserDAO


@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: any

userDao = UserDAO()
childDao = ChildDAO()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    identifier = data.get('username')  # username o email
    password = data.get('password')

    user = userDao.login(identifier, password)

    response = ApiResponse(
        msg="login",
        coderesponse="1",
        data=user
    )

    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )

    return jsonify(asdict(response)), 200

@app.route('/child', methods=['POST'])
def child():
    token = request.headers.get('apikey')
    user=None
    if (token):
        user=userDao.getUserByToken(token)
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)), 400
    
    data = request.get_json()
    childs = childDao.getChilds(user['id'])
    response = ApiResponse(
            msg="getChilds",
            coderesponse="1",
            data=childs
        )
    return jsonify(asdict(response)), 200

if __name__ == '__main__':
    app.run(debug=True)