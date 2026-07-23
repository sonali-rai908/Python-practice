# write a program to open three files  1.txt , 2.txt ,3.txt . if any these files are not prsent , a messsage without exiting the program must be printed prompting the same
# use of exception handling

# using for loop
files = ["1.txt","2.txt","3.txt"]

for file in files:
    try:
        with open (file,"r") as f:
            print(f"Contents of file {file}: ")
            print(f.read())

    except FileNotFoundError:
        print(f"File {file} is not present")

#without using for loop
try:
    with open("1.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("1.txt is not present.")

try:
    with open("2.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("2.txt is not present.")

try:
    with open("3.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("3.txt is not present.")


print("thank you!")