import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentuser = {}
        
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    print(user)
        
    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanıcı Oluşturuldu")
    def login(self,username,password):
        for user in self.users:
            if username ==username and user.password==password:
                self.isLoggedIn = True
                self.currentuser =user
                print("Login Yapıldı")
                break
    def identity(self):
        if self.isLoggedIn :
            print(f"username : {self.currentuser.username}")
        else:
            print("giriş yapılmadı") 
    def logout(self):
        self.isLoggedIn = False
        self.currentuser ={}
        print("Çıkış Yapıldı")
    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open("user.json","w")as file:
            json.dump(list,file)
    

repository =  UserRepository()
while True:
    print("Menü".center(50,"*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\n Seçiminiz:")
    if secim=="5":
        break
    else:
        if secim =="1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")

            user = User(username = username, password = password ,email = email)
            repository.register(user)

            print(repository.users)
        elif secim =="2":
            username = input("Username: ")
            password = input("Password: ")
            repository.login(username, password)
        elif secim =="3":
            repository.logout()
        elif secim =="4":
            repository.identity()
        else :
            print("Yanlış Seçim")
