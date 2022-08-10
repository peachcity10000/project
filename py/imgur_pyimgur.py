import pyimgur

CLIENT_ID = "eddf91499480c3b"
PATH = "./static/temp/LINE_ALBUM_2022623_220624_3.jpg" #A Filepath to an image on your computer"
title = "Uploaded with PyImgur"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title=title)
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.type)
