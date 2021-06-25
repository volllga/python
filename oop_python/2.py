# class A:
#     def __init__(self, i=2, j=3):
#         self.i = i
#         self.j = j
#
#     def __str__(self): # переопределяет функцию принт
#         return "A"
#
#     def __eq__(self, other):
#         return self.i * self.j == other.i *other.j
#
#
# def main():
#     x = A(1, 2)
#     y = A(2, 1)
#     print(x == y, x , y,   )
#
#
# main()

# #Code1
# number = 9
# if number % 2 == 0:
#     even = True
# else:
#     even = False
# print("Code1: even := {}".format(even))
#
# #Code2
# even = True if number % 2 == 0 else False
# print("Code2: even := {}".format(even))
#
# # Code3
# even = number % 2 == 0
# print("Code3: even := {}".format(even))

# class A:
#     def __init__(self):
#         self.x = 1
#         self.__y = 1
#
#     def getY(self):
#         return self.__y
#
# a = A()
# a.x = 45
# a.__y = 77
# print(a.x, a.__dict__, a.getY())
# #
# x = 2
# y = 1
# x *= y + 1
# print(x)

# def f1(x=1, y=2):
#     x = x + y
#     y += 1
#     print(x, y)
# f1(y=2, x=1)

# d = {'a':40, 'b':44}
# print(list(d.keys()))

class parent:
    def __init__(self, param):
        self.v1 = param

class child(parent):
    def __init__(self, param):
        self.v2 = param

obj = child(11)
print("%d %d" % (obj.v2, obj.v2))