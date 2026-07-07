# Function with parameter
def goodDay(name):
   print("Good Day !", name)

goodDay("Sonali")    
goodDay("Nitin")


def info(name,age):
    print(name,age)
    print("Name: ",name)

info("Sonali","19")  # positional argumnets - as here position matters 
info("Sonal","25")   # first value goes to first parameter ,second value goes to second parameter

info(age=20,name="Sonali")  # keyword arguments - you will get acces using keywords ,, position not matters


#default arguments
def greet(name="Freind"): # default value of name will be freind
    print("Hello! ", name)

greet()    #as nothing mentioned here then it will print the default value
greet("Sonali")