#!/usr/bin/env pyhon

import random

male = False
male = bool(random.randint(0, 1))

if (male):
    print('jozko')
else:
    print('lenka')

print('*****')

print(bool(True))
print(bool(False))
print(bool("text"))
print(bool(""))
print(bool(" "))
print(bool(0))
print(bool(1))
print(bool(3))
print(bool(None))

def function():
    # print('hello')
    # return('hello')
    pass #returns None 

print('*****')

val = function()

print(val)

baskets = 16
apples = 24

total = apples * baskets

print("there are total of", total, "apples")
print(f"there are total of {total} apples") #the best
print("there are total of %d apples" % total)
print("there are total of {} apples".format(total))