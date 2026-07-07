# write a recursive a function to print the sum of first n natral numbers

def sum_n(n):
    if n==1:
        return 1
    return n + sum_n(n-1)

number=int(input("Ente the value of n : "))
sum=sum_n(number)
print("Sum=",sum)   