# whn a single child inherit methods and atributes from two or more parent classes
class Employee:            # Base class
    company="Infosys"
    def show(self):        # parent class function which can be used by inherited class
        print("\nhelo there! i am base class.")

class coder:
    language="python"        # second base class
    def printlanguage(self):
        print("\nhello there ! i am second base class.")
        print(f"Language : {self.language}")

class programmer(Employee,coder):   #Inherited class or child class
   # company="infotech"         # if company is not mentioned here and you run b.company then output will be infosys
    def showlanguage(self):     # inherited class function which can oly used by this class
        print(f"\nThe company in which i work is {self.company} and the language which i use is {self.language}.")

a=Employee()
A=coder()
b=programmer()
print(a.company,A.language,b.language,b.company)

a.show()

A.printlanguage()

b.show() 
b.printlanguage()           
b.showlanguage()  