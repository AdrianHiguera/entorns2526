from dataclasses import dataclass, asdict
import hashlib
from flask import jsonify
import mysql.connector
import uuid
from time import time
import random

class UserDAO:
    
    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection

    def login(self, identifier, password):
        # connexio a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query="""
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """

        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user
    
    def setTokenUser(self, username):
        # connectar BBDD
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        # generar token
        token=self.getHash()

        # update a BBDD cap token al usuari per username
        query = "UPDATE User SET token ='" + token + "'WHERE username = %s" + username
        print(query)
    
        cursor.execute(query)
        con.commit()

        # close BBDD
        cursor.close()
        con.close()

    def getHash2(self,username):
        milliseconds = str(time()*1000)
        data = username + milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
    
    def getHash(self):
        milliseconds = str(time()*random.randrange(10000))
        data = milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()

dao=UserDAO()
print(dao.getHash("User1"))

u=dao.login("masdasfare", "pare")
print(u)

milliseconds = str(time()*1000)
print("Time in milliseconds since epoch", milliseconds)
data = "Hola Mundo" + milliseconds
print(data)

hash_object = hashlib.sha256(data.encode('utf-8'))
token = hash_object.hexdigest()
print(token)
