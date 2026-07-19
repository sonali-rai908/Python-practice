class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __eq__(self, other):
        return self.n == other.n

    def __truediv__(self,other):
        return self.n / other.n

    def __floordiv__(self,other):
        return self.n // other.n

    def __str__(self):
        return f"Number is {self.n}"


n= Number(20)
m= Number(10)
print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)
print(n==m)
print(n,m)

#Jab bhi koi operator kisi object ke saath use hota hai, 
# Python us operator ki corresponding magic method (dunder method) ko call karta hai.
