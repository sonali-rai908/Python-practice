name = "Sonali"
age = 20

print("My name is {} and I am {} years old.".format(name, age))

print("{1} {0}".format("Sonali", "Hello"))

print("Name: {name}, Age: {age}".format(name="Sonali", age=20))

# number formating
pi = 3.14159265

print("{:.2f}".format(pi))

#real life example
product = "Laptop"
price = 55000

print("Product: {} | Price: ₹{}".format(product, price))

#  but nowadays it is not much more used ....as now f_string is mostly used
name = "Sonali"
age = 20

# format()
print("My name is {} and I am {}.".format(name, age))

# f-string
print(f"My name is {name} and I am {age}.")

# f-strings are generally preferred in modern Python because they are more readable, concise, and often faster. format() is still useful, especially in older codebases or when formatting strings dynamically.