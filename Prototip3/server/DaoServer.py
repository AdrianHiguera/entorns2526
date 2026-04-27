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
    
    def getUserByToken(self, token):
        con= self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE token = %s
        """
        cursor.execute(query, (token,))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user

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
    
class ChildDAO:

    def getChilds(self, username):
        return "TODO getChilds for " + username


dao = UserDAO()
u = dao.getUserByToken("fa7cc6e2d8d3a5e178888eba42de2f5640fbc39816e741be73467b264382998a")
print(u)