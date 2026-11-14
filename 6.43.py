prev = float(input("Введите число (1000 - конец последовательности): "))
x = float(input("Введите число (1000 - конец последовательности): "))
k = 0
distinct = 1
in_group = False
while x != 1000:
    if x == prev:
        if not in_group:
            k = k + 1
            in_group = True
        k = k + 1
    else:
        distinct = distinct + 1
        in_group = False
    prev = x
    x = float(input("Введите число (1000 - конец последовательности): "))
print("Количество чисел, равных соседним:", k)
print("Количество различных чисел:", distinct)
