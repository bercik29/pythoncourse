#!/usr/bin/env pyhon

import sys
import os

dir_name = sys.argv[1]

gfiles = os.walk(dir_name)

for (root, dir, files) in gfiles:
    for file in files:
         if file.endswith("py"): 
                print("{0} ".format(file)) 
