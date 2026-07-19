# craete a class 'Employee' and add salary and increment properties to it
# write a method 'salaryAfterIncrement' methos with aproperty decorator with a settre
# which changes the value of increment based on the salary

class Employee:
    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment

    @property   
    def salaryAfterIncrement(self):
        return self.salary + (self.salary*self.increment/100)

    

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,new_salary):
        self.increment =( ((new_salary -self.salary)/self.salary)*100 )
    
    def show(self):
        print(f"\nSalary : {self.salary}\nIncrement : {self.increment}%")
        print(f"Salary After Increment : {self.salaryAfterIncrement}")

    

    

e = Employee(50000,10) # Creating object
e.show()

e.salaryAfterIncrement=60000

print("\nAfter using setter: ")
e.show()     # show method again
