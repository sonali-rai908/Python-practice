#Write a program to filter a list of numbers which are divisible by 5.

# 1 - method
l=[5,7,10,8,9,15,20,25]

a = list(filter(lambda x: x%5==0 , l ))
print(a)

# 2 method
def divisible5(n):
    if(n%5==0):
        return True
    return False

f = list(filter(divisible5,l))
print(f)