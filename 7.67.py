n = int(input("Введите количество пар n: "))
a = float(input("Введите a1: "))
b = float(input("Введите b1: "))
max_sum = a + b
min_prod = a * b
for i in range(2, n + 1):
    a = float(input(f"Введите a{i}: "))
    b = float(input(f"Введите b{i}: "))
    if a + b > max_sum:
        max_sum = a + b
    if a * b < min_prod:
        min_prod = a * b
print("а) Максимальная сумма чисел в паре:", max_sum)
print("б) Минимальное произведение чисел в паре:", min_prod)
