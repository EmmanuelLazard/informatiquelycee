# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur=500
hauteur=500
for x in range(largeur):
    for y in range(hauteur):
        r,v,b=img.getpixel((x,y))
        n_r=255-r
        n_v=255-v
        n_b=255-b
        img.putpixel((x,y),(n_r,n_v,n_b))
img.show()
