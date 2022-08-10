from imgurpython import ImgurClient
from datetime import datetime

import csv

class imgurObj:
    def __init__(self):
        with open('./static/imgur/imgur.csv' , encoding='utf-8') as f:
            imgur_list = list(csv.reader(f))
            self.client_id = imgur_list[0][1]
            self.client_secret = imgur_list[1][1]
            self.access_token = imgur_list[2][1]
            self.refersh_token = imgur_list[3][1]
            self.album = imgur_list[4][1]
            self.image_dict = {}
    
    def uploadImage(self,imgAddr):
        try:
            client = ImgurClient(
                self.client_id, 
                self.client_secret,
                self.access_token,
                self.refersh_token
                )
            config = {
                'album': self.album,
                'name': 'peachCity',
                'title': 'title',
                'description': f'test-{datetime.now()}'
            }
            self.image_dict = client.upload_from_path(imgAddr, config=config, anon=False)
            return 0
        except:
            return -1
    
    def getImageAddr(self):
        return self.image_dict['link']
        