class Employee:            # Base class
    company="Infosys"
    def show(self):        # parent class function which can be used by inherited class
        print("helo there!")

class programmer(Employee):   #Inherited class or child class
    company="infotech"         # if company is not mentioned here and you run b.company then output will be infosys
    def showlanguage(self):     # inherited class function which can oly used by this class
        print("hiiii !")

a=Employee()
b=programmer()
print(a.company,b.company)

a.show()
b.show()            # base clas function used by inherited class
b.showlanguage()