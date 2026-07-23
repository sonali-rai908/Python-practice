class Workers:           
    salary = 20000      
    state = "UP"

    def getinfo(self):
        print(f"The salary is {self.salary} and the state of worker is {self.state}.")
    
    @staticmethod    # static method doesnt need any object . it is marked as decorator
    def greet():      # no need of self here as it is termed as static method
        print("Hello")

w1 = Workers()
w1.getinfo()
w1.greet()

''' when we call w1.getinfo(), python internally treats it like Workers.getinfo(w1) , means it always takes one argument 
 here as w1 , so we have to mention it through self keyword . self simply means "this current object'''
