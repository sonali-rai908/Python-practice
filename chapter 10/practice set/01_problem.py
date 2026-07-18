# craete a class "Programmer " for storing information about few programmers working at microsoft

class Programmer:
    company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

        print(f"\nInformation of programmer {self.name}__")

p1=Programmer("Rohan",120000,233227)
print(f"\nCompany= {p1.company}\nName = {p1.name}\nSalary = {p1.salary}\nPIN = {p1.pin}")   
p2=Programmer("Soham",130000,233234)  
print(f"\nCompany= {p2.company}\nName = {p2.name}\nSalary = {p2.salary}\nPIN = {p2.pin}")