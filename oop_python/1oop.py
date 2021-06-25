def square(number):
    return number ** 2

a, b, c = map(square, (map(int, input().split())))
print(a, b, c)
