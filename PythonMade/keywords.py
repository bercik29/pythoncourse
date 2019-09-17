#!/usr/bin/env pyhon

grades = ["A", "B", "C"]

grade = input('Enter grade: ')

if grade.upper() in grades:
    print('there it is')

if grade.upper() not in grades:
    print('wroooong')

value = not (True and False)
print(value)

import numpy as alias
import math
print(math.pi)

from math import pow as tryout

print(tryout(9,2))
print(alias.random.randint(1, 10), end = " " )
print()