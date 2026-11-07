import math

s1 = float(input("Введите площадь круга: "))
s2 = float(input("Введите площадь квадрата: "))
r = math.sqrt(s1 / math.pi)
a = math.sqrt(s2)

# а)
if 2 * r <= a:
    print("а) Да, круг уместится в квадрате")
else:
    print("а) Нет, круг не уместится в квадрате")

# б)
if a * math.sqrt(2) <= 2 * r:
    print("б) Да, квадрат уместится в круге")
else:
    print("б) Нет, квадрат не уместится в круге")
