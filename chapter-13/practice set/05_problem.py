#Write a program to find the maximum of the numbers in a list using reduce().

from functools import reduce

l= [56,16,28,9,10,36,19]

def greater(a,b):
    if(a>b):
        return a
    return b

r= reduce(greater,l)
print(r)

a= reduce(lambda x,y :x if x>y else b,l)
print(a)