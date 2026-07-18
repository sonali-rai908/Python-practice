#write a class "calculator" capable of finding square , cube and squrae root ofa number
class Calculator:
    maths_functions="Square,Cube and Square root"

    def __init__(self,number):
        self.number=number
        print(self.maths_functions)
        print(f"\nSquare of {number} = {number**2}")
        print(f"Cube of {number} = {number**3}")
        print(f"Square root of {number} = {number**1/2}", end="\n\n")

n1=Calculator(5)




class Calculator:
    maths_functions="Square,Cube and Square root"

    def __init__(self,number):
        self.number=number
        
    def square(self):
        print(f"\nSquare of {self.number} = {self.number**2}")

    def cube(self):
        print(f"Cube of {self.number} = {self.number**3}")

    def squareroot(self):
        print(f"Square root of {self.number} = {self.number**1/2}")

n1=Calculator(5)
print(n1.maths_functions)
n1.square()
n1.cube()
n1.squareroot()

