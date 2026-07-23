'''Functions in pyhton are blocks of reusable code that perform a specific task 
    Instead of writing the same code again and again ,you can write it once inside a function and call it whenever needed
     When program gets bigger i size we use functions'''

# Function without parameters
def greet():
    print("Hello!")  # Functn definition

greet()    # Function call
print("Python")
greet()  #it depends on us that how many times we want to run the function 

# Function with parameter
def goodDay(name):
   print("Good Day !", name)

goodDay("Sonali")    
goodDay("Nitin")

#function with return
def add(a,b):
    return a+b

a=int(input("Enter a number :"))
b=int(input("Enter the second number: "))    
result=add(a,b)
print(result)


#taking input inside the function
def avg():
    a=int(input("Enter a number: "))
    b=int(input("Enter second number: "))

    average=(a+b)/2
    print("Average: ", average)

avg() 
print("Thank u!")

avg()   
avg()