#a class method is a method which is bound to the class and not the object of the class

class Employee:
    a=1
    def show(self):
        print(f"The class attribute of a is {self.a}")

e=Employee()
e.a=43
e.show()   # it will show 43 as self access the current instance attribute , if not mentioned tehn class attribute


# so if we want to access or calss attribute whether instance atribute is give or not then we use @classmethod
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e=Employee()
e.a=4
e.show()