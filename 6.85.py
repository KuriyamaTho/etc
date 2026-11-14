n = int(input("Введите натуральное число: "))
pos2 = 0
pos5 = 0
i = 0
while n > 0:
    i = i + 1
    if n % 10 == 2:
        pos2 = i
    if n % 10 == 5:
        pos5 = i
    n = n // 10
if pos2 > 0 and pos5 > 0:
    if pos2 > pos5:
        print("Цифра 2 расположена левее цифры 5")
    else:
        print("Цифра 5 расположена левее цифры 2")
else:
    print("В числе нет обеих цифр 2 и 5")
