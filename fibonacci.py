#!/usr/bin/env python

"""
A module containing the fibonacci
function.
"""

def fib(n):

    a, b = 0, 1
    
    while b < n:
    
        print(b, end=" ")
        (a, b) = (b, a + b)


# testing

def main():
    n = input('Write number ')
    num = int(n)
    fib(num)

if __name__ == '__main__':
    main()