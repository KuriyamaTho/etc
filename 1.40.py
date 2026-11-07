import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
x = (2 / (a ** 2 + 25) + b) / (math.sqrt(b) + (a + b) / 2)
y = (abs(a) + 2 * math.sin(b)) / (5.5 * a)
print("x =", x)
print("y =", y)
