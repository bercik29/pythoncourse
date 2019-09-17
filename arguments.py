#!/usr/bin/env pyhon

import sys

print('script name:', sys.argv[0])
print('arguments:', end=' ')

for arg in sys.argv[1:]:
    print(arg, end=" ")
   
print()

print(sys.copyright)

val = 12
print(dir(val))

print(sys.__doc__)

print(sys.platform)
print(sys.version)

print(val.to_bytes(2, byteorder='big'))