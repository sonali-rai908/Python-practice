#===============
# try and except -- we can tell python - "Try this code . If an error occurs, dont crash. Handle it."
#===============

try:
    num = int(input("Enter a number : "))
    print(100/num)

except:
    print("Something went wrong.")      # program will not crash ..error will be handled 

#==============================
# catching specific exception
#==============================

try:
    a =int(input("Enter a number: "))
    print(100/a)

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero..")

except ValueError as v:
    print(v)
    print("please enter a valid integer.")