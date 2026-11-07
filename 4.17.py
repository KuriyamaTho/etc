import math

s1 = float(input("Введите площадь круга: "))
s2 = float(input("Введите площадь равностороннего треугольника: "))
r = math.sqrt(s1 / math.pi)
a = math.sqrt(4 * s2 / math.sqrt(3))
r_in = a * math.sqrt(3) / 6
r_out = a / math.sqrt(3)

# а)
if r <= r_in:
    print("а) Да, круг уместится в треугольнике")
else:
    print("а) Нет, круг не уместится в треугольнике")

# б)
if r_out <= r:
    print("б) Да, треугольник уместится в круге")
else:
    print("б) Нет, треугольник не уместится в круге")
