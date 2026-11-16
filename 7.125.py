prev = float(input("Введите число 1: "))
distinct = 1
for i in range(2, 31):
    x = float(input(f"Введите число {i}: "))
    if x != prev:
        distinct = distinct + 1
    prev = x
print("Количество различных чисел:", distinct)
