import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число (неотрицательное): "))
if math.sqrt(b) < a:
    b = b * 5
print("Первое число:", a)
print("Второе число:", b)
