file=open("data.txt","r")
print(file.read())
file.close()

# The same can be written using wuth statement like this:
with open("data.txt") as file:
    print(file.read())

# you dont have to close the file explicitily
