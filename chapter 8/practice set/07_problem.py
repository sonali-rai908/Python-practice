# write a pyhton function to remove  agiven word from a list and strip it at the same time
'''def remove_and_strip(list,word):
    new_list=[]
    for item in list:
        if item!=word:
            new_list.append(item.strip(word))  # strip can only remove the characters if they are at end,,if rohan becomes rohani then it cant strip an from it
    return new_list

list=["sonali","rohani","an","subham"]                
print(remove_and_strip(list,"an"))'''


''' this question actually means that strip(means remove whitespaces from the beginning and end of words)
    all the items of list and then remove a word'''

def remove_and_strip(list,word):
    new_list=[]
    for items in list:
        items.strip()
        if word.strip()!=items.strip():
            new_list.append(items.strip())   
    return new_list

list=["sonali"," rohani "," an ","subham"]                
print(remove_and_strip(list," an "))    # here there are whitespaces also present in word so to match it with we should also use strip wih the method with word to match with it

