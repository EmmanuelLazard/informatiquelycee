# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("test.jpg")
largeur=800
hauteur=533
for x in range(0,largeur):
    for y in range(0,hauteur):
        r,v,b=img.getpixel((x,y))
        r=255-r
        v=255-v
        b=255-b
        img.putpixel((x,y),(r,v,b))
img.show()
img.save("res_test.jpg","JPEG")
