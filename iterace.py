#!/usr/bin/env python

# iterator.py

stri = "formidable"

for e in stri:
   print(e, end=" ")

print()

it = iter(stri)

print(next(it))
print(next(it))
print(next(it))

print(list(it))

mytuple = ("apple", "banana","pear")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


def countdown(num):
    print('Starting')

    while (num > 0):
        yield num
        num -= 1

for val in countdown(10):
    print(val)

