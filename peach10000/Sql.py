import sqlite3
from peach10000 import post

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

    def insert_post(self , post:post.post):
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

    def is_user_valid(self, userName):
        command = f"SELECT * from account where account_id = '{userName}';"
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        self.close_sql()
        if(len(row)>0):
            return True
        else:
            return False

    def is_password_correct(self, userName, password):
        command = f"SELECT * from account where account_id = '{userName}';"
        if (self.connected ==False):
            self.connection()
        self.cursor.execute(command)
        self.db_conn.commit()
        row = list(self.cursor.fetchall())
        self.close_sql()

        if(row[0][3]==password):
            return True
        else:
            return False