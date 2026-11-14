n = int(input("Введите натуральное число: "))
a = int(input("Введите цифру a: "))
b = int(input("Введите цифру b: "))
pos_a = 0
pos_b = 0
i = 0
while n > 0:
    i = i + 1
    if n % 10 == a and pos_a == 0:
        pos_a = i
    if n % 10 == b and pos_b == 0:
        pos_b = i
    n = n // 10
if pos_a > 0 and pos_b > 0:
    if pos_a < pos_b:
        print("Цифра a расположена правее цифры b")
    elif pos_a > pos_b:
        print("Цифра b расположена правее цифры a")
    else:
        print("Цифры a и b совпадают")
else:
    print("В числе нет обеих цифр a и b")
