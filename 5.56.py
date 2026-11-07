n = int(input("Введите натуральное число n: "))
a = float(input("Введите a1: "))
sum_abs = abs(a)
prod_abs = abs(a)
alt = a
sign = -1
prev = a
print("в) Суммы соседних чисел:")
for i in range(2, n + 1):
    a = float(input(f"Введите a{i}: "))
    sum_abs = sum_abs + abs(a)
    prod_abs = prod_abs * abs(a)
    alt = alt + sign * a
    sign = -sign
    print(prev + a)
    prev = a
print("а)", sum_abs)
print("б)", prod_abs)
print("г)", alt)
