a = int(input("Введите размер a: "))
b = int(input("Введите размер b: "))
while b != 0:
    print("Квадратов со стороной", b, ":", a // b)
    r = a % b
    a = b
    b = r
