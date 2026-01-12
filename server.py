from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username", default="")
    # Si els parametres OK
    if username!="":
    # Anar al DAO Server i cercar User per username
    # Respondre amb dades Usuari si trobat
        reposta="username"+username
    else:# Si els parametres NO ok
    # Respondre error
        reposta="username No Informat"
    return "Json Sortida getUserName"

if __name__ == '__main__':
    app.run(debug=True)
