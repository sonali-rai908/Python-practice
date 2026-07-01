list=[1,2,3,2,1]
# a=list.index(1)
# b=list.index(1)
# if a==b:
#     print("List is palindrome")
# else:
#     print("The list is not palindrome ")   
new_list = list.copy()
new_list.reverse()
if(list==new_list):
    print("Palindrome")
else:
    print(" n palindrome")

