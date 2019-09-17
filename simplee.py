#!/usr/bin/python3

"""
This is a simple module
"""

# __doc__

def main():
    a = [1, 2, 3]

    print(__file__)

    a.append(3)

    for e in a:
        print(e)

if __name__ =='__main__':
    main()