#!/usr/bin/env python

# inheritance.py

class Animal:

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        # super().__init__()
        
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()