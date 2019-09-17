#!/usr/bin/env pyhon

import numpy

vals = numpy.linspace(100, 1000, 900, dtype = int)
print(vals)

vals2 = []

for i in range(100, 1001):
    vals2.append(i)

print(vals2)



def seq():
    x = 100
    stop = 1001
    while (x < stop) :
        x += 1
        yield x



for x in seq():
    print(x)
