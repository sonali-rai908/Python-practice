#The global keyword is used inside a function to tell Python:
#"I want to use and modify the global variable, not create a new local variable."

a=89        # global variable
def show():
    a=3     # local varibale
    print(a)

show()    
print(a)  # it will represent the gloabl varible which will not change

# if you want modify the global varible in the function , you hav eto use global keyword
def fun():
    global a
    a=3
    print(a)

fun()
print(a)   # now a will become 3 