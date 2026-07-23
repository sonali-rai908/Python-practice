def add (a,b):
    return a+b

print(add(10,20))

# lambda is a keyword which helps us to create afunction usimg an expression
add = lambda a,b : a+b 
print(add(10,20))

# for one entry
square =lambda x:x*x
print(square(5))

#for three entries
multiply = lambda a, b, c: a*b*c

print(multiply(2,3,4))

# lambda allows only one expression ..multilple statements are not allowed 

#example
def maximum(a,b):
    if a>b:
        return a
    else:
        return b

print(maximum(40,20))

#using lambda
maximum = lambda a,b: a if a>b else b
print(maximum(10,20))


# def - used for large functios that include multiple statements
# lambda - used for one line expresson functions