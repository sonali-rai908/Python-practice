#  a dictionary in python is a colection of key value pairs
#  mutable - they can be changed  
#  keys must be unique 
# it is unordered 
# it is indexed 

d={} # emoty dictionary
student={
    "name":"Sonali",
    "age":20,
    "branch":"CSE",
}
print(student)

# value can be accessedusing keys
print(student["name"])
print(student["age"])

#we can add new pairs to it 
student["college"]="AZAD"
print(student)

#updating values 
student["age"]=21 
student.update({"age":22,"university":"AKTU"}) # there are two ways to update the values 
print(student)
print(len(student))

# deleting a item
del student["branch"]
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.pop("age"))

#  We can get the values of keys by two ways 
#  1- using student("name")
#     in this ...if we write a keys which isnot existed thennit will show error
#  2- using student.get("name")   
#     in thus if we write a keys which is not existed then it will return  none 
 
# print(student.clear()) 
print(student.copy())
print(student.popitem()) # it willshow an error because i had used clear first which had already cleared the dictionary
                        #   dictionary is empty 
                        # it is used to remove And return the last inserted key value pair from a dictionary
                        # it doesnt require any argument 