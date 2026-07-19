# 1- @property(Getter) : used to get the values of an attribute

class student:
    def __init__(self,marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

# 2- @<property>.setter - used to set or update value

    @marks.setter                 
    def marks(self,value):
        if value<=100:
            self._marks=value
        else:
            print("invalid marks")

# 3- @<property>.deleter - used when an attribute is deleted
    
    @marks.deleter
    def marks(self):
        print("marks deleted")
        del self._marks

s = student(90)
s.marks=200
print(s.marks)
del s.marks


#example
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

emp = Employee("Sonali", "Rai")
emp.first="anjali"

print(emp.email)


# Exam tip: Property decorators are commonly used for encapsulation in Object-Oriented Programming.
#  They let you validate or compute values while allowing users of your class to use simple attribute syntax (obj.attribute) 
# instead of method calls (obj.get_attribute()).
