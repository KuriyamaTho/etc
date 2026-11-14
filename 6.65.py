pos = 0
prev = int(input("Введите a1: "))
i = 1
while i < 15 and pos == 0:
    x = int(input(f"Введите a{i + 1}: "))
    i = i + 1
    if x == prev:
        pos = i - 1
    prev = x
if pos > 0:
    print("Да, первая пара одинаковых соседних чисел:", pos, "и", pos + 1)
else:
    print("Нет, одинаковых соседних чисел нет")
