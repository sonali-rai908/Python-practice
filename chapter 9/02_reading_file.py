file = open("file.txt")   # read is a deafult mode , if you not mention anything it will open in read mode
#data = file.read()  # reads the whole file
#print(data)

#if file doesnot exist -- FileNotFoudError

#print(file.read(8))  # read first 8 characters

# readline()
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

