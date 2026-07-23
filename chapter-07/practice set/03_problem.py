# multiplication table using while loop 
n=int(input("Enter the number:"))

print(f"Table of {n}")

i=1
while (i<=10):
    print(f"{n} * {i} = {n*i}" )
    i+=1