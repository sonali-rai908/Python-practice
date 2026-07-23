class Workers:           
    salary = 20000      
    state = "UP"

    def __init__(self,name,salary):     # dunder method which is automatically called
        self.name=name
        self.salry=salary
       # print("I am creating an object")

    def getinfo(self):
        print(f"The salary is {self.salary} and the state of worker is {self.state}.")
    
    
w1 = Workers("Rohan",130000)
w2= Workers("Soaham",30000)
print(w1.name,w1.salary)
print(w2.name,w2.salary)

w1.getinfo()


