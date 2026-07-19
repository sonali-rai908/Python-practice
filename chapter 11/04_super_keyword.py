class school:
    def __init__(self):
        print("constructor of school")
    
class Class(school):
    def __init__(self):
        super().__init__() 
        print("constructor of class")
    
class Student(Class):
    def __init__(self):
        super().__init__()           # it will run the constructor of parent class too
        print("constructor of student")
    
    
#a=school()
a=Class()
a=Student()

# if we use only self then objects will run only therre ow constructors 
# but if we want to use the constructor of parent class in inherited class then we use super key word

# super() method is used to access the methods of a super class in the derived class
# __init__() calls the constructor of the base class