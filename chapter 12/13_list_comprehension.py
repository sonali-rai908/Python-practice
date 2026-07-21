# normally 

list = [1,2,3,5,9,3,4]

squaredList = []
for item in list:
    squaredList.append(item*item)

print(squaredList)

# all this can be done in a single line using list comprehension

cubeList = [i**3 for i in list]
print(cubeList)