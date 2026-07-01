# WAP to find out whther a student is passed or failed if it require total of 40 % and at least 35% in each subject to pass.
# assume three subjects and take marks as input from the user 
marks1=int(input("Enter the marks of first subject:"))
marks2=int(input("Enter the marks of second subject:"))
marks3=int(input("Enter the marks of third subject:"))

# chaeck for total percentage
total_percentage=((marks1+marks2+marks3)/300)*100

if (total_percentage>=40 and marks1>=35 and marks2>=35 and marks3>=35):
    print("Congratulations! \nYou are passed.")

else:
    print(f"You failed.\nTry again next year!\nEven your total percentage is:{total_percentage},you failed")