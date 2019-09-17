#!/usr/bin/env pyhon

from PIL import Image
from pathlib import Path
import os

home_dir = str(Path.home())
directories = os.walk(home_dir)

for root, dirs, files in directories:
    # print(dirs)
    for file in files:
        if file.endswith("jpg") or file.endswith("png"):  
            # pass
            try:
                img = Image.open(os.path.join(root, file))
                print("{0} \tFormat: {1}\tSize: {2}\tMode: {3}".format(file, img.format, 
                     img.size, img.mode))
            except:
                print('-------------- Unable to identify file {0} ----------------------------'.format(file))
            #  os.path.join(root, file)

