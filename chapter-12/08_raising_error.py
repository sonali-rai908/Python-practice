a= int(input("Enter a number: "))
b=int(input("Enter second number: "))

if  (b==0):
    raise ZeroDivisionError("Hey dont you know that zero cant divide any number.")

else:
    print(a/b)

# raise with try and except

try:
    age = -2

    if age < 0:
        raise ValueError("Negative age is not allowed.")

except ValueError as e:
    print(e)
