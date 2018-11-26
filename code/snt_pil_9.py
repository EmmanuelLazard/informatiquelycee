# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
largeur_image=500 
hauteur_image=500
for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b=img.getpixel((x,y))
        if b<200:
            n_b=255-b
        img.putpixel((x,y),(r,v,n_b))
img.show()
