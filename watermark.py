#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys

try:
    sid = Image.open("sid.jpg")

except:
    print("Unable to load image")
    sys.exit(1)
    
idraw = ImageDraw.Draw(sid)
text = "Sid Vicious"

font = ImageFont.truetype("arial.ttf", size=90)

idraw.text((10, 10), text, font=font)
 
sid.save('sid_watermarked.png')