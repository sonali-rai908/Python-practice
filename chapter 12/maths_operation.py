def add(a,b):
    return a+b

#print("maths_operation.py is running")
#print(__name__)   # for maths_operation.py output will be __main__ as it is the main file
                   # but for main.py file output will be maths_operation as it is imported from here
                   # means __name__ will make us know thath which is the main file and which one imports it

# so if we dont want to run the code of this main file into imported one then

if (__name__ == "__main__"):     # this checks is this file run directly?
    print("We are dirctly running this code")    # now this code will only run when you are here
    print("maths_opertion.py is running")
    
