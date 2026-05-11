from User import *
from DaoUserClient import *

class ViewConsole:

    daoClient=DaoUserClient()
    token=""
    current_child=None
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Taps")
        print("5: Quit")
        while(True):
            option=input("Enter Option: ")
            if option.isdigit():  # <- añadir () para llamar al método
                optionInt=int(option)
                if optionInt > 0 and optionInt < 6:
                    return optionInt
            print("Error: Introdueix una opció correcta, només números")

        
    def viewGeneral(self):
        option=-1
        while(True):
            option=self.viewShowMenu()
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    self.viewLoginToken(self.token)
                case 3:
                    self.viewChilds(self.token)
                case 4:
                    self.viewTaps(self.token)
                case 5:
                    exit()


    def viewChilds(self, token):
        print("View Childs")
        resposta_childs = self.daoClient.childToken(token)
        if resposta_childs:
            for i, child in enumerate(resposta_childs):
                print(f"{i+1}: {child['child_name']} (id: {child['id']})")
            
            opcio = input("Selecciona un child: ")
            if opcio.isdigit():
                index = int(opcio) - 1
                if 0 <= index < len(resposta_childs):
                    self.current_child = resposta_childs[index]
                    print(f"Child seleccionat: {self.current_child['child_name']}")
                else:
                    print("Opció no vàlida")
            else:
                print("Opció no vàlida")
        else:
            print("No s'han pogut obtenir els childs")
        

    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user=self.daoClient.loginToken(token)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")

    def viewTaps(self, token):
        if self.current_child is None:
            print("Primer has d'anar a l'opció 3 i seleccionar un child")
            return
        
        id_child = self.current_child['id']
        print(f"Obtenint taps del child: {self.current_child['child_name']} (id: {id_child})")
        
        taps = self.daoClient.getTaps(token, id_child)
        if taps:
            for tap in taps:
                print(tap)
        else:
            print("No s'han pogut obtenir els taps")


viewConsole=ViewConsole()
viewConsole.viewGeneral()
