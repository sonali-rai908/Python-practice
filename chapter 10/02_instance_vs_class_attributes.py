

class Workers:           
    salary = 20000      # class attributes
    state = "UP"


w1 = Workers()
w1.name = "Rohan"        #instance attribute
w1.state = "Bihar"        # state will now become bihar
print(w1.name,w1.salary,w1.state)

w2 = Workers()
w2.name = "Mohan"
w2.salary = 30000          # now salary will be 30000 at the palce of 20000 (instance attribute over class attribute)
print(w2.name,w2.state,w2.salary)

# Instance attributes , take preference over class atributes during asignment and retrieval
