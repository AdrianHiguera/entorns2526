from DaoUserClient import DaoUserClient, User


class ViewConsole:

    def __init__(self):
        self.daoClient = DaoUserClient()
        self.loggedUser = None

    def viewShowMenu(self):

        print("\n1: Login")
        print("2: Quit")

        while True:

            option = input("Enter Option: ")

            if option.isdigit():

                optionInt = int(option)

                if 1 <= optionInt <= 2:
                    return optionInt

            print("Error: Introdueix una opció correcta")

    def viewGeneral(self):

        option = -1

        while option != 2:

            option = self.viewShowMenu()

            match option:

                case 1:
                    self.viewLogin()

                case 2:
                    print("Adeu")

    def viewLogin(self):

        print("\nEnter username or email and password")

        username = input("Username: ")
        password = input("Password: ")

        user = User("", username, password, "", "", "")

        resposta = self.daoClient.login(user)

        if resposta:

            self.loggedUser = resposta

            print("\nLogin correcte:", resposta)

            childs = self.daoClient.getChilds(self.loggedUser)

            if childs:

                print("\nChilds del usuari:")

                for c in childs:
                    print(f"- {c['child_name']} | Sleep average: {c['sleep_average']}")

            else:
                print("No hi ha childs")

        else:
            print("Error login")


if __name__ == "__main__":
    view = ViewConsole()
    view.viewGeneral()