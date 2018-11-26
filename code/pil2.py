# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur=500
hauteur=500
for x in range(0,largeur):
    for y in range(0,hauteur):
        r,v,b=img.getpixel((x,y))
        img.putpixel((x,y),(255,v,b))
img.show()
img.save("res_pomme.jpg","JPEG")
