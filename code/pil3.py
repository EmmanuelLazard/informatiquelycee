# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur=500
hauteur=500
for x in range(0,largeur):
    for y in range(0,hauteur):
        r,v,b=img.getpixel((x,y))
        img.putpixel((x,y),(b,r,v))
img.show()
img.save("res_pomme_3.jpg","JPEG")
