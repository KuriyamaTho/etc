a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
if (a + b) % 2 == (c + d) % 2:
    print("Да, поля одного цвета")
else:
    print("Нет, поля разного цвета")
