#write a program to print third , fifth and seventh element from a list using enumerate function

list = ["Apple","Banana","Grapes","Mango","Orange","Kiwi","Pineapple" ]

for index,item in enumerate(list):
    if index==2 or index == 4 or index == 6 :
        print(item)


# if we want to take user input and then print the result
l=[]

n = int(input("Enter the number of elements : "))

for i in range(n):
    element = int(input("Enter number:"))
    l.append(element)

for index,number in enumerate(l):
    #if index==2 or index == 4 or index == 6 :
    if index in(2,4,6):
        print(number)


