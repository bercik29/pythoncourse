#!/usr/bin/env pyhon

valx = "x"
valc = "č"

valz = valx + valc

print(len(valx))
print(len(valc))
print(valz, len(valz))
print('***********')
print('length of', valx, 'is', len((valx).encode('utf8')))
print('length of', valc, 'is', len((valc).encode('utf8')))
