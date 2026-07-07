# write a program to calculate the grade of a student from his marks from the following scheme :
# 90-100= extraordinary
# 80-90=A 
# 70-80=B 
# 60-70=C 
# 50-60=D
# <50=F 

marks=int(input("Enter the marks:"))

if(marks>=90 and marks<=100):
    
    Grade="Extraordinary"

elif(marks>=80 and marks<=90):
    
    Grade="A"    

elif(marks>=70 and marks<=80):
    
    Grade="B"        

elif(marks>=60 and marks<=70):
    
    Grade="C"        

elif(marks>=50 and marks<=60):
    
    Grade="D"      

elif(marks<=50):
    
    Grade="F" 

else:
    
    print("Failed")          


print("Your grade is:",Grade)    