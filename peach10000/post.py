from peach10000 import User
import time

class post:
    def __init__(self) :
        self.title = ''
        self.context = ''
        self.position = [-100,-100,-100,-100]
        self.author_id = ''
        self.photo_addr = ''
        self.date = 0
        self.tel = ''
        self.web = ''
    
    def judge_filled(self):
        if self.title == '': return False
        if self.context == '': return False
        if self.author_id == '': return False
        if self.photo_addr == '': return False
        if self.date == 0: return False
        if self.position[0] ==-100: return False
        return True

    def setTitle(self, title:str):
        try:
            self.title = title
            return 0
        except:
            return -1
    
    def setContext(self , context:str):
        try:
            self.context = context
            return 0
        except:
            return -1
    
    def setAuthorId(self , AuthorId:str):
        try:
            self.author_id = AuthorId
            return 0
        except:
            return -1
    
    def setPosition(self , position:list):
        try:
            len(position)==4
            self.position = position
            return 0
        except:
            return -1

    def setAuthor(self , user:User):
        try:
            self.author_id = user.userName
            return 0 
        except:
            return -1

    def setPhotoAddr(self , addr:str):
        try:
            self.photo_addr = addr
            return 0
        except:
            return -1
    
    def setdate(self):
        try:
            self.date = time.time()
            return 0
        except:
            return -1
    
    def setTel(self , tel:str):
        try:
            self.tel = tel
            return 0
        except:
            return -1

    def setWeb(self , web:str):
        try:
            self.web = web
            return 0
        except:
            return -1
        
        