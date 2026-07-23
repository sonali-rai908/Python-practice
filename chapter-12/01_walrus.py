# it is just like a assignment operater .... which is used to assign expressions to the vraiable

# normall asignment(=)
x=10
print(x)     # first value is assigned and then used

#walrus operator(:=)
print(x:=11)  # 11 is assigned to x and printed in the same line


# EXAMPLE
# 1- Without walrus 
name = input("Enter your name: ")

if len(name) > 5:
    print(name)

# 2- with walrus
if((name:=input("Enter your name :")) and len(name)>5):
    print(name)