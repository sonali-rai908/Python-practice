# a conditional expression is used to make a decision in a program based on whether the condition is true or false 
#if...else anf if..elif..else  two types of conditional expressions 

a=int(input("Enter your age:"))

 # there can be multiple if else statements 
# if statement no 1 
if(a%2==0):
    print("a is even")
#end of if statement no 1 as there is no else further here ....its over you that you can add else statement here  

#if statement no 2
if (a>=18):
    print("You are eligible to vote .")
    print("Now you can do whatever you want.")

elif(a<0):
    print("Are you mad ? Why are you entering neagtive age?")   

elif(a==0):
    print("Then you are just born .\nYou cant even walk then how can you go to vote.")

else:
    print("You are not eligible to vote.")    
#end of statement no 2    

print("END")    

# ternary(conditional) expressions
# python also provides a one line conditional expression
age=20
result="Adult" if age>=18 else"Minor"
print(result)