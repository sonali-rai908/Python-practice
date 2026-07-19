'''In Python, property decorators (@property) allow you to access methods like attributes (variables).
 They are mainly used to control getting, setting, and deleting an attribute while keeping the syntax simple.'''

# without @property
class Employee:
    def get_salary(self):
        return 300000


e = Employee()
print(e.get_salary())  #method call


#with @property
class Employee:
    @property
    def get_salary(self):
        return 300000

e = Employee()
print(e.get_salary) # looks like an attribute , we odnt have to write it as get_salary() like methods , we can simply write it like get_salary just like an variable or attribute


