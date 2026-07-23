# store the multiplication tables generated inproblem 3 in a file named Tables.txt
n= int(input("Enter the number: "))

tableList=[f"{n} * {i} = {n*i} "for i in range(1,11)]

with open("Tables.txt","a") as f:
    f.write(f"Table of {n} :\n")
    for line in tableList:
        print(line)
        f.write(line+ "\n" )