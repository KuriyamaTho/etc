import math

a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
p = 2 * (a + b)
d = math.sqrt(a ** 2 + b ** 2)
print("Периметр =", p)
print("Длина диагонали =", d)
