# write a program to find whether a given username contains less than 10 characters or not 
username=input("Enter your username:")

if (len(username)<10):
    print("Characters are less than 10:",len(username))

else:
    print("Characters are more than or equal to 10:",len(username))    