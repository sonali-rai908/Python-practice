# INPUT() FUNCTION
# The input() function is used to take input from the user.
#
# By default, input() always returns the user's input as a string (str),
# unless we explicitly convert it into another data type.
#
# Example:
# If the user enters 2 and 4, Python stores them as "2" and "4" (strings).

a = input("Enter number 1: ")
b = input("Enter number 2: ")

print("Number 1 is:", a)
print("Number 2 is:", b)

# Since a and b are strings, the + operator concatenates them instead of
# performing mathematical addition.
# Example: "2" + "4" results in "24".
print(a + b)


# To perform mathematical operations, we need to convert the input into
# an appropriate numeric data type, such as int or float.

c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))

# int() converts the string returned by input() into an integer.
# Now the + operator performs mathematical addition.
# Example: 2 + 4 results in 6.
print(c + d)


# IMPORTANT:
# input() → always returns a string by default.
# int(input()) → converts user input into an integer.
# float(input()) → converts user input into a decimal number.