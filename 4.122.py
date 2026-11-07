a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
if a < b + c and b < a + c and c < a + b:
    print("Да, треугольник существует")
else:
    print("Нет, треугольник не существует")
