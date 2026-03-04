import requests
from DaoServer import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://localhost:5000"

    def login(self, user):

        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }

        response = requests.post(URL_peticio, json=params_POST)

        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw['coderesponse']

            if code_response == '1':
                user = User(
                    user_data_raw['id'],
                    user_data_raw['username'],
                    "",
                    user_data_raw['email'],
                    user_data_raw['idrole'],
                    user_data_raw['token']
                )
                return user   
            else:
                return None
        else:
            return None

daoClient = DaoUserClient()
user = User("", "mare", "12345", "", "", "")
resposta = daoClient.login(user)
print(resposta)