import os
from PIL import Image


directory = 'D:/Projekty/Python/Studia/folder_testowy'
for image in os.listdir(path=directory):
    if os.path.splitext(image)[1] == '.png':
        Image.open(directory + '/' + os.path.splitext(image)[0] + ".png").convert('RGB')\
                   .save(directory + '/' + os.path.splitext(image)[0]+".jpg")
