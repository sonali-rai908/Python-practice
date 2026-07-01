# WAP to find greatest of four numbers entered by user
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))

if(a>=b and a>=c and a>=d):
    print("The greatest number:",a)

elif(b>=a and b>=c and b>=d):
    print("The greatest number:",b)

elif(c>=a and c>=b and c>=d):
    print("The greatest number:",c)

else:
    print("The greatest number:",d)        