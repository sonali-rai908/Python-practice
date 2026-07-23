# factorial of a given number
n=int(input("Enter the number: "))

mul=1
for i in range(1,n+1):
    mul*=i

print(f"Factorial of {n} is {mul}")  