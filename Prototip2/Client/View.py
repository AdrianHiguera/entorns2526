class ViewConsole:

    def viewShowMenu(self):

        print("1: Login")
        print("2: Quit")

        while True:

            option = input("Enter Option: ")

            if option.isdigit():

                optionInt = int(option)

                if optionInt >= 1 and optionInt <= 2:
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

        print("Enter username or email and password")

        username = input("Username: ")
        password = input("Password: ")

        return username, password
    
