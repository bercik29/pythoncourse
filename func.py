#!/usr/bin/env python

# global_variable2.py

name = "Jack"


def f():

    global name
    name = "Robert"
    print("Within function", name)


print("Outside function", name)
f()
print("Outside function", name)