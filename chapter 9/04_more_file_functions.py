# readline()
file=open("file.txt","r")
print(file.readline()) # read only one line at a time
#print(file.readline())

# readlines()
lines=file.readlines()  #returns all the lines in the form of  a list
print(lines)
print(type(lines))

# if we want to print all the lines in different line the use strip()
for line in lines:
    print(line.strip())

file.close()

