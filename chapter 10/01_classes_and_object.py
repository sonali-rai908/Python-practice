# class - a blueprint or template 
# object- a real instance of a class

class Workers:           
    salary = 20000      # class attributes
    state = "UP"


w1 = Workers()
w1.name = "Rohan"        #instance attribute
print(w1.name,w1.salary,w1.state)

w2 = Workers()
w2.name = "Mohan"
print(w2.name,w2.state,w2.salary)

''' Here name is object attribute or instance attribute(different for all objects) and 
salary and state are class attributes (same for all objects) as they directly belong to the class'''