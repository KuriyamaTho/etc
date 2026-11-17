import math


def triangle(a, b, c):
    p = (a + b + c) / 2
    return a + b + c, math.sqrt(p * (p - a) * (p - b) * (p - c))


a1 = float(input("Первый треугольник, сторона a: "))
b1 = float(input("Первый треугольник, сторона b: "))
c1 = float(input("Первый треугольник, сторона c: "))
a2 = float(input("Второй треугольник, сторона a: "))
b2 = float(input("Второй треугольник, сторона b: "))
c2 = float(input("Второй треугольник, сторона c: "))
p1, s1 = triangle(a1, b1, c1)
p2, s2 = triangle(a2, b2, c2)
print("Сумма периметров:", p1 + p2)
print("Сумма площадей:", s1 + s2)
