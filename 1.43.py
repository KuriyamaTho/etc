import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Среднее арифметическое модулей =", (abs(a) + abs(b)) / 2)
print("Среднее геометрическое модулей =", math.sqrt(abs(a) * abs(b)))
