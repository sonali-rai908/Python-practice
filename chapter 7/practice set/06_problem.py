#sum of first n ntural numbers using while loop
n=int(input("Enter a number:"))

print(f"Sum of first {n} numbers : ") 

i=0
sum=0
while(i<=n):
    sum+=i
    i+=1

print(sum)    