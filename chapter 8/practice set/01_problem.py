# write a program using function to find geatest of three numbers '''

# method 1 - easy method
def greatest():                                      # function definition
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: ") )
    c=int(input("Ente the third number: "))

    if(a>=b and a>=c):
        print(f"{a} is greatest")
    elif(b>=a and b>=c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

greatest()                                             # function call

# method 2- preferable method in interviews
def greatest(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c

print(greatest(2,5,4))     # function with prameters

a= int(input("Enter first number: "))   
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

print(greatest(a,b,c))

''' second method is consudered as better method ,
     in this the function has only one responsibility that to dind the greatest number 
     you can reuse it with different values without asking for input every time '''

print(greatest(8,78,48)) # you can use it for many entries
print(greatest(32,76,91))     