class school:
    school_name="ABC School"
    
class Class(school):
    Class = "2nd"
    def show_school(self):
        print(f"\nMy school name is : {self.school_name}\nThe class in which i study is : {self.Class}")

class Student(Class):
    student_name="rohan"

    def show(self):
        print(f"\nSchool name : {self.school_name}\nClass : {self.Class}\nStudent name : {self.student_name}")

s1=Class()
s1.show_school()

s2=Student()
s2.show()
s2.show_school()