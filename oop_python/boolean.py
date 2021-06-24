a, b = map(int, input().split())
print(a % 7 == 0 and b % 7 == 0)


x = int(input())
print(5 < x and x <= 19)

a, b = input(), input()
print(a == "awesome" or b == "awesome")

x = int(input())
print(x // 10 > 0 and x // 100 < 1)

print(9 < int(input()) < 100)

def square(number):
    return number ** 2

a, b, c = map(square, (map(int, input().split())))
print(a+b==c or a+c==b or b+c==a)

f = sorted(map(int,input().split()))
print(f[0]**2 + f[1]**2 == f[2]**2)