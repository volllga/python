print("Hello")
class Point3D:
    x = 1
    y = 2
    z = 3


point = Point3D()
print("Position number one:", point.__dict__, Point3D.__dict__)

point.x = 10
print("Position number two:", point.__dict__, Point3D.__dict__)

setattr(Point3D, "x", 11)
print("Position number three:", point.__dict__, Point3D.__dict__)
print(point.x, point.y, point.z)

delattr(Point3D, "z")
print("Position number four:", point.__dict__, Point3D.__dict__)