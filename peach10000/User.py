from flask_login import  UserMixin
from peach10000 import post, Sql

class user():
    def __init__(self) -> None:
        self.userName = ''
        self.password = ''
        self.id = ''

    def setUserName(self, username:str):
        self.userName = username
        self.id = username
    
    def checkLogin(self, username, password):
        db = Sql.peachDB()
        if ( db.is_user_valid(userName = username) == True):
            self.userName = username
            self.id = username  
            return db.is_password_correct(userName = username, password = password)

    def checkUser(self, username):
        db = Sql.peachDB()
        return db.is_user_valid(userName = username)

class flask_login_user(UserMixin):
    pass