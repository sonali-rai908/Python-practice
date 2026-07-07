# write a program to find whether a given set of number is even number

n=int(input("Enter the number :"))

print(f"All even numbers from 1 to {n} are:")
for i in range(1,n+1) :
    if(i%2)==0:
           print(i) 