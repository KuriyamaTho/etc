m = int(input("Введите натуральное число m: "))
n = int(input("Введите натуральное число n: "))

# 1-й способ
a = m
b = n
while b != 0:
    r = a % b
    a = b
    b = r
lcm = m * n // a
x = lcm
print("1-й способ:")
while x <= m * n:
    print(x)
    x = x + lcm

# 2-й способ
x = m
while x % n != 0:
    x = x + m
lcm = x
print("2-й способ:")
while x <= m * n:
    print(x)
    x = x + lcm
