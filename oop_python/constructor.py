class Point3D:

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        print(self.__dict__)


point = Point3D()
point = Point3D(3)
print("Please, input three int: ")
x, y, z = input(), input(), input()
point2 = Point3D(x, y, z)

dict = point2.__dict__

for i in dict:
     print(dict.get(i), end=" ")
