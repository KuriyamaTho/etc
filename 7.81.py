n = int(input("Введите n (n >= 3): "))
prev = int(input("Введите x1: "))
x = int(input("Введите x2: "))
s = prev + x
max_s = s
min_s = s
max_pos = 1
min_pos = 1
prev = x
for i in range(3, n + 1):
    x = int(input(f"Введите x{i}: "))
    s = prev + x
    if s > max_s:
        max_s = s
        max_pos = i - 1
    if s <= min_s:
        min_s = s
        min_pos = i - 1
    prev = x
print("а) Максимальная сумма двух соседних чисел:", max_s)
print("б) Минимальная сумма двух соседних чисел:", min_s)
print("в) Номера чисел первой пары с максимальной суммой:", max_pos, max_pos + 1)
print("г) Номера чисел последней пары с минимальной суммой:", min_pos, min_pos + 1)
