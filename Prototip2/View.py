

class ViewConsole:

    def viewShowMenu(self):
        print("1: Login")
        print("2: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit):
                optionInt=int(option)
                if(option >= 1 and option < 2):
                    return optionInt

            print("Error: Introdueix una opció correcta")

    def viewGeneral(self):
        option=-1
        while(option!=2):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                case 2:
                    #quit
                    print("Adeuuuuuuuuuu")

    def viewLogin(self):
        print("View login")
        print("Enter username or email and password to login.")
        username = input("Username or email: ")
        password = input("Password: ")
        return username, password