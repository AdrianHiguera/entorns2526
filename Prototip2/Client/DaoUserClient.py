import requests

class User:
    def __init__(self, id, username, password, email, idrole, token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token

    def __str__(self):
        return f"{self.username} ({self.email})"


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

            if user_data_raw["coderesponse"] == "1":

                data = user_data_raw["data"]

                user = User(
                    data["id"],
                    data["username"],
                    "",
                    data["email"],
                    data["idrole"],
                    data["token"]
                )

                return user

        return None
    
    def getChilds(self, user):

        URL_peticio = self.base_URL + "/child"

        headers = {
            "Authorization": user.token
        }

        params_POST = {
            "iduser": user.id
        }

        response = requests.post(URL_peticio, json=params_POST, headers=headers)

        if response.status_code == 200:

            data_raw = response.json()

            if data_raw["coderesponse"] == "1":
                return data_raw["data"]

        return None


# TEST
'''daoClient = DaoUserClient()
user = User("", "mare", "12345", "", "", "")

resposta = daoClient.login(user)

print(resposta)'''