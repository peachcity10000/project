from imgurpython import ImgurClient
from datetime import datetime

def upload(client_data, album , name = 'test-name!' ,title = 'test-title' ):
    config = {
        'album':  album,
        'name': name,
        'title': title,
        'description': f'test-{datetime.now()}'
    }
    print("Uploading image... ")
    image = client_data.upload_from_path("./static/temp/LINE_ALBUM_2022623_220624_3.jpg", config=config, anon=False)
    print("Done")
    return image


if __name__ == "__main__":
    client_id ='f79a118fc40f407'
    client_secret = 'b672dcc13ca6a9eb3b08d43b4ffedf7344d0d3d1'
    access_token = "3252482ed707dabbd72c786c5c0cdce6c5058f53"
    refresh_token = "4d88dbf5c9b70ddc523bff6ff0dfea55890efa39"
    album = "X0TEAzQ"

    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    image = upload(client_data = client, album=album)
    print(type(image))
    print(f"圖片網址: {image['link']}")