# nornmall what we do is -----

l = ["apple","banana","grapes"]

index = 0
for fruits in l:
    print(f"The fruit at index {index} : {fruits}")
    index += 1

# the same can be printed as 
for i in range(len(l)):
    print(i,l[i])


#============================
# now using enumerate keyword - it creates a pair of index and value
#============================

fruits =["apple","banana","grapes"]
print(list(enumerate(fruits)))      # it gives key value pair of index and items in a form of list

# now using for loop we can unpack them and print separately
for index,item in enumerate(fruits):
    print(index , item)

# By default, indexing starts from 0.
for index,item in enumerate(fruits, start=1):
    print(index , item)
# now t will start from 1

#for strings
name="Sonali"
for index,letters in enumerate(name):
    print(f"The letter at index {index} is {letters}")

# real life example
courses = ["Python", "Java", "C++", "JavaScript"]

for number, course in enumerate(courses, start=1):
    print(f"{number}. {course}")