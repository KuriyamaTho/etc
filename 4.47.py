a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
if a == b or a == c or b == c:
    print("Да, треугольник равнобедренный")
else:
    print("Нет, треугольник не равнобедренный")
