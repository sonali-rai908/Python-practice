#  a set in python is an unordered collection of unique elements 
#  they do not allow duplicate values and are mutable 
#  you can add or remove elements
# order is not always maintained 
# indexing not allowed

a={1,3,4,7,3,9 , "apple"} # duplicates will be removed in output......order may vary
print(a)

e=set() # this will create an empty set ...you shoukd have to keep in  mind that s={} will create an empty dict but not the set
print(type(e))

# adding an element
a.add("orange")
print(a )

#removing an element
a.remove("orange") # raises an error if not found 
print(a)

#discard also used to remove an element 
a.discard("orange")   # it will not raise an error if not found
print(a)


#check if an element exist 
if "apple" in a:
    print("apple is present")

#length of set
print(len(a))

a.clear()
print(a)


# set operations
A={1,2,3,4,5}
B={4,5,6,7,8}
print("Union:",A.union(B))
print("Union can also be find as:",A|B)

print("Intersection",A.intersection(B))
print("Intersection can also be find as:",A&B)

print("the differeence of two sets will be :",A-B)  # RETURNS THE ELEMENT THAT ARE IN A BUT NOT IN B

print("Symmetric difference is:",A^B)   # RETURNS THE ELEMENT THAT ARE IN EITHET SET BUT NOT IN BOTH 

print({1,2}.issubset(A))
print(A.issubset(B))
print(A.issuperset({1,2,9}))





