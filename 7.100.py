n = int(input("Введите натуральное число n: "))
m = int(input("Введите m: "))
p = int(input("Введите p: "))
s = 0
for i in range(1, n + 1):
    d = int(input(f"Введите d{i}: "))
    if d <= m:
        s = s + d
if s % p == 0:
    print("Да, сумма чисел, не превышающих m, кратна p")
else:
    print("Нет, сумма чисел, не превышающих m, не кратна p")
