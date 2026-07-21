#write a list comprehension to print a list which contains the multiplication table of a user entered number

n= int(input("Enter the number: "))

tableList=[n*i for i in range(1,11)]
print(tableList)


# if we want i aform of table then 
n= int(input("Enter the number: "))

tableList=[f"{n} * {i} = {n*i}"for i in range(1,11)]


for line in tableList:
    print(line)                      # we are just unwrapping the list and printinf eache elements of list separately