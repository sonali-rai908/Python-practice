# create a class 'Pets' from aclass 'Animals' and further create a class 'Dog' 
# from 'Pets' . Add a method 'bark' to class 'Dog'

class Animal:
    def __init__(self):
        print("Animal class constructor")

class Pets(Animal):
    def __init__(self):
        super().__init__()
        print("Pets class constructor")

class Dogs(Pets):
    def __init__(self):
        super().__init__()
        print("Doga class constructor")

    def Barks(self):
        print("Dog barks!")

d=Dogs()     # Creating object
d.Barks()     # Calling bark method
        


# simple way 
class Animal:
    pass

class Pet(Animal):
    pass

class Dog(Pet):

    @staticmethod
    def Barks():
        print("Bow Bow!")

d=Dog()
d.Barks()