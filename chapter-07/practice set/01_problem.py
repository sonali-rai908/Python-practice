# multiplication table of a given number using for loop

n=int(input("Enter of the number of which table you want:"))
print(f"Table of{n}")

for i in range(1,11,1):
    print(f"{n} * {i} = {i*n}") 