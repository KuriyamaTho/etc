prev = float(input("Введите число 1: "))
k = 0
distinct = 1
in_group = False
for i in range(2, 21):
    x = float(input(f"Введите число {i}: "))
    if x == prev:
        if not in_group:
            k = k + 1
            in_group = True
        k = k + 1
    else:
        distinct = distinct + 1
        in_group = False
    prev = x
print("Количество чисел, равных соседним:", k)
print("Количество различных чисел:", distinct)
