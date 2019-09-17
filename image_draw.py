#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont 

img = Image.new('RGBA', (200, 200), 'white')    
idraw = ImageDraw.Draw(img)

idraw.rectangle((10, 10, 100, 100), fill='blue')

font = ImageFont.truetype("arial.ttf", size=20)

idraw.text((20, 50), 'Hello', font=font)
 
img.save('rectangle.png')