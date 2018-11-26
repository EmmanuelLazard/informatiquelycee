# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur=500
hauteur=500
for x in range(0,largeur):
    for y in range(0,hauteur):
        r,v,b=img.getpixel((x,y))
        n_r=v
        n_v=b
        n_b=r
        img.putpixel((x,y),(n_r,n_v,n_b))
img.show()
