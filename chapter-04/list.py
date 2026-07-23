fruits=["Apple" , "Banana" , 5 , 3.56 , False ,"Akash"]
print(fruits)
print(fruits[0])  # indexing is same as strings 

fruits[0]= "Grapes" # list are mutable ....there elements can be change further ....unlike string ...
print(fruits) # this will become your updtaed list .... now the further methods will be applied to it 

print(fruits[0:2]) # list slicing ae also same as strings

fruits.append("sonali")
print(fruits) # append method is used to add items to list 

l1=[2,4,1,7,2,9,10]   # duplaicates are also allowed in lists
l1.sort()           # sort method is used to sort the list in ascending order
print(l1)

l1.reverse()
print(l1)

fruits.insert(2,"ananya")   # this method is also used to add items to the list but it add items where you want 
                            # it will insert at the mentioned index
print(fruits)                            

item_at_index_2_in_fruits=fruits.pop(2) # it removes the element from the index which is mentioned 
print(item_at_index_2_in_fruits) # it can also return the value t at gven index which it will pop out
print(fruits)

fruits.remove("Grapes")
print(fruits)  # it removes the given item 