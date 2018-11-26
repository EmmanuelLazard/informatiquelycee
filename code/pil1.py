# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur=500 
hauteur=500
for x in range(0,largeur):
    for y in range(0,hauteur):
        r,v,b=img.getpixel((x,y))
        g=int((r+v+b)/3)
        img.putpixel((x,y),(g,g,g))
img.show()
img.save("pomme_g.jpg","JPEG")
