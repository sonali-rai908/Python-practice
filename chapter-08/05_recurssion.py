''' recursion is a technique in which a function calls itself to solve a probelm
 a recursion function must have:
                                1- Base case= the condition that stops the recursion
                                2- Recursive case= the part where the function calls itself

without a base case , the function will keep calling itself forever and cause an recurssionerror '''

def factorial(n):
    if (n==1 or n==0):     # base case
        return 1
    return n* factorial(n-1)    # recursive case

n=int(input("Enter the number : "))
print(f"Factorial of {n} = {factorial (n)}")   

