''' write a program to generate multiplication tables from 2 to 20 and write it to the different files
    place this files in a foler for a 13 yr old.'''

def generatetable(n):
    with open(f"Tables/tables_{n}.txt","w") as file:
            file.write(f"Multiplication table of  {n}:\n") 
            for i in range(1,11):
                     file.write(f"\n{n} * {i} = {n*i}")

for i in range(1,21):
    generatetable(i)

