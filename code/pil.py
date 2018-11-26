# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("test.jpg")
exif_data = img._getexif()
for key, value in exif_data.items():
        if type(value)!=bytes:
            print("code ",key," : ",value)
