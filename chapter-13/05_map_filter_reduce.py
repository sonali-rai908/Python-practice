# all three works on iterables(list,tuples etc) and mainly used with lambda function

# map ()   ___apply sma efunction on each element
# normally-
numbers = [1,2,3,4,5,7]

square=[]
for number in numbers:
    square.append(number**2)

print(square)

# using methods
square = list(map(lambda x : x**2,numbers))
print(square)

# filter() __ checks condition and only keeps that element which fulfills the condition

even=list(filter(lambda x:x%2 == 0, numbers))
print(even)

# reduce() __ list ke sare elements ko combine krke ek hi value return krta h
from functools import reduce

numberss = [1,2,3,4,5,6,7]
result = reduce(lambda x,y: x+y , numberss)
print(result)


# real life example
marks = [35, 40, 55, 80, 90]

# bonus +5 to everyone
print(list(map(lambda x: x+5, marks)))

# Passed students (marks ≥ 40)
print(list(filter(lambda x : x>=40, marks)))

#total marks
print(reduce(lambda x,y : x+y, marks))
