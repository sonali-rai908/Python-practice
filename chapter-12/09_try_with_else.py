# sometimes we want to run a piece of code whn try was successfull
try:
    a=int(input("Enter a number: "))
    print(a)

except ValueError as e:
    print(e)

else:
    print("try is sucessfully executed!")  # else will execute when and only when try will sucessfull
