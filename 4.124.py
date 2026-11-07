import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
if a < b + c and b < a + c and c < a + b:
    s = sorted([a, b, c])
    if math.isclose(s[0] ** 2 + s[1] ** 2, s[2] ** 2):
        kind = "прямоугольный"
    elif s[0] ** 2 + s[1] ** 2 > s[2] ** 2:
        kind = "остроугольный"
    else:
        kind = "тупоугольный"

    # а)
    print("а) Вид треугольника:", kind)

    # б)
    if a == b and b == c:
        feature = "равносторонний"
    elif a == b or a == c or b == c:
        feature = "равнобедренный"
    else:
        feature = "разносторонний"
    print("б) Вид и особенности треугольника:", kind + ",", feature)
else:
    print("Треугольника с такими сторонами не существует")
