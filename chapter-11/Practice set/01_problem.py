# create aclass 2d vector and use it to create another class representing a 3 d vector

class Vector2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"2-D Vector = ({self.i}i {self.j}j)")

class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"3-D Vector = ({self.i}i {self.j}j {self.k}k)")

v2 =  Vector2D(2,3)
v2.show()

v3=Vector3D(3,6,7)
v3.show()