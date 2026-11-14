prev = float(input("Введите число (0 - конец последовательности): "))
x = float(input("Введите число (0 - конец последовательности): "))
distinct = 1
while x != 0:
    if x != prev:
        distinct = distinct + 1
    prev = x
    x = float(input("Введите число (0 - конец последовательности): "))
print("Количество различных чисел:", distinct)
