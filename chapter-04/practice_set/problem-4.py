# write a program to sum a list in pyhton 
# using sum() function
numbers = [10,20,30,49,90]
total=sum(numbers)
print(f"the sum of the list is :{total}")

# without using sum function
total=0
for n in numbers :
    total=total+n

print("The sum of list is :",total)    