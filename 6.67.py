pos = 0
prev = int(input("Введите a1: "))
i = 1
while i < 20 and pos == 0:
    x = int(input(f"Введите a{i + 1}: "))
    i = i + 1
    if x % 2 == 1 and prev % 2 == 1:
        pos = i - 1
    prev = x
if pos > 0:
    print("Да, первая пара соседних нечетных чисел:", pos, "и", pos + 1)
else:
    print("Нет, пар соседних нечетных чисел нет")
