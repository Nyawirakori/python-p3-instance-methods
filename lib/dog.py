#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self): #self allows methods to access the other methods and attributes
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()
snoopy.sit()
