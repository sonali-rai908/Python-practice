file=open("file.txt","r")

line=file.readline()

while(line != ""):
    print(file.readline())

file.close()