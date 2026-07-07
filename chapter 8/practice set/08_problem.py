# python function to print multiplication table

def table(n):
    
    for i in range(1,11):
        #return n*i   #is not useable here because return immeditely stops teh function and sends back just one value n*i
        print(f"{n} * {i} = {n*i}")


       

n=int(input("Enter a number: "))        
table(n)