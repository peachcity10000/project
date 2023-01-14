import sqlite3
import time

from click import command

class user:
    def __init__(self) -> None:
        self.userName = ''

    def setUserName(self, username:str):
        self.userName = username



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

    def setAuthor(self , user:user):
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
        
        


class peachDB:
    def __init__(self) :
        self.DATABASE = 'peachCity.db'
        self.connected = False

    def connection(self):
        self.db_conn = sqlite3.connect(self.DATABASE)
        self.connected = True
        self.cursor = self.db_conn.cursor()

    def select_photoText(self):
        command = 'SELECT post_title, post_context , post_photo_addr from post;'
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        return row[0]

    def insert_post(self , post:post):
        return 

    def close_sql(self):
        if(self.connected == True):
            self.db_conn.close()
        self.connected = False

    def get_html_id_info(self, html_id:str):
        verification_code  = html_id.split('-')[0]
        if (verification_code!= 'g16913'):
            return "error"
        
        command = f'SELECT * from store where store_html_id = "{html_id}";'
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        return row[0]

    def getPost(self, html_id:str):
        verification_code  = html_id.split('-')[0]
        if (verification_code!= 'g16913'):
            return "error"
        
        command = f'SELECT * from post where post_store_id = "{html_id}";'
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        return row[0]

    def getAllPost(self ):
        command = f'SELECT * from post'
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        return row

    def getImgur(self, html_id:str):
        verification_code  = html_id.split('-')[0]
        if (verification_code!= 'g16913'):
            return "error"
        
        command = f'SELECT * from img where store_id = "{html_id}";'
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        return row[0]
