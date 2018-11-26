# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open("pomme.jpg")
img.putpixel((250,250),(255,0,0))
img.show()
