# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur_image=500 
hauteur_image=500
for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b=img.getpixel((x,y))
        n_v=255-v
        img.putpixel((x,y),(r,n_v,b))
img.show()
