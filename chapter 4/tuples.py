# same as list but immutable
a=() #empty tuple
print(type(a))

b=(4,)   # to print a single entry in tuple we should have to use a comma after writing it 
print(type(b))      # if we dont write the comma after single entry then it will treated as integer 

c=(1,2,3, 3, False,"sonali","rohit")
# c[0]=8  # tuple object does not support item assignment means the elments cant be changed once after they are created
# print(c)

# tuple in pyhton are immutable thats why they have only two builtin methods 
# 1- count()
# 2- index()

no = c.count(3)
print("count of 3 =",no)

index_3=c.index(3)
print("index of 3=",index_3)

# operations with tuple 
# 1- concatenation
result=c+b
print("concatenation of two tples c and b will be :",result)

# 2-repetiton 
print("repeat the tuple b three times:",b*3)

# 3-membership
print(3 in c)

# 4-lenght
print(len(c))

# 5- min and max
d=(3,4,5,6,1,9,10)
print(min(d))
print(max(d))

# 6-slicing
print(d[1:4])

# 7-unpacking
my_tuple=("Sonali",20,"India")
name,age,country=my_tuple
print(name)
print(age)
print(country)

# 8-extneded unpacking       collections the remaining elements in to alist 
my_tuple_2=(1,2,3,3,3,4,5,6,7,8)
a,*b,c=my_tuple_2
print(a)
print(b)
print(c)