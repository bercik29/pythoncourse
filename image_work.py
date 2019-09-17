#!/usr/bin/env pyhon

from PIL import Image, ImageFilter, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys

try:
    sid = Image.open('sid.jpg')

except IOError:
        print('no image')
        sys.exit(1)

# sid.show()
# print("Format: {0}\nSize: {1}\nMode: {2}".format(sid.format, 
#   sid.size, sid.mode))

blurred = sid.filter(ImageFilter.BLUR)

blurred.save("sid-blurred.png")

sid.save('sid.png', 'png')  

pngsid = Image.open('sid.png')
# pngsid.show()

# print("Format: {0}\nSize: {1}\nMode: {2}".format(pngsid.format, 
#     pngsid.size, pngsid.mode))

grayscale = sid.convert('L')
# grayscale.show()

cropped = sid.crop((100, 100, 350, 350))
cropped.save('sid_cropped.jpg')
# cropped.show()

rotated = sid.rotate(180)
rotated.save('sid_rotated.jpg') 
rotated.show()