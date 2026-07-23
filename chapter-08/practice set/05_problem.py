'''write  a python program to print first n lines of the following pattern
    ***
    **
    *      for n=3  '''

def star_pattern(a):
    if a==0:
        return

    print("*"*a)
    star_pattern(a-1)    
        

print(star_pattern(4))    

''' *
    **
    *** for n=3 '''

def pattern(n):
    if n==0:
        return
    pattern(n-1)
    print("*"*n)   

print(pattern(4))            