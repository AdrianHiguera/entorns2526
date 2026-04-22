from dataclasses import dataclass, asdict
import hashlib
from flask import Flask, jsonify, request
import mysql.connector
from time import time
import random
from werkzeug.security import generate_password_hash, check_password_hash

# =======================
# CONFIG FLASK
# =======================

app = Flask(__name__)

# =======================
# DAO
# =======================

class UserDAO:
    
    def connectBBDD(self):
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="tapatapp"
        )

    def login(self, identifier, password):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s)
        """

        cursor.execute(query, (identifier, identifier))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            print("LOGIN OK")
            token = self.setTokenUser(user['username'])
            user['token'] = token
        else:
            print("LOGIN FAIL")
            user = None

        cursor.close()
        con.close()

        return user

    def setTokenUser(self, username):
        con = self.connectBBDD()
        cursor = con.cursor()

        token = self.getHash(username)

        query = "UPDATE User SET token = %s WHERE username = %s"
        
        cursor.execute(query, (token, username))
        con.commit()

        cursor.close()
        con.close()

        return token

    def getHash(self, username):
        milliseconds = str(time() * 1000)
        data = username + milliseconds
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def getHash2(self):
        milliseconds = str(time() * random.randrange(10000))
        return hashlib.sha256(milliseconds.encode('utf-8')).hexdigest()


# =======================
# RESPONSE
# =======================

@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: any


# =======================
# DAO INSTANCE
# =======================

userDao = UserDAO()


# =======================
# ROUTES
# =======================

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    identifier = data.get('username')  # username o email
    password = data.get('password')

    user = userDao.login(identifier, password)

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


# =======================
# MAIN
# =======================

if __name__ == '__main__':
    app.run(debug=True)