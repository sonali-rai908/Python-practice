# add a static method i problem 2 to greet users with hello 
class Calculator:
    maths_functions="Square,Cube and Square root"

    def __init__(self,number):
        self.number=number

    @staticmethod
    def greet():
        print("Hello !")
        
    def square(self):
        print(f"\nSquare of {self.number} = {self.number**2}")

    def cube(self):
        print(f"Cube of {self.number} = {self.number**3}")

    def squareroot(self):
        print(f"Square root of {self.number} = {self.number**1/2}")

n1=Calculator(5)
n1.greet()
print(n1.maths_functions)
n1.square()
n1.cube()
n1.squareroot()

