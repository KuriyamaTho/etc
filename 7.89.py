n = int(input("Введите натуральное число n: "))
b = int(input("Введите b: "))
s = 0
for i in range(1, n + 1):
    x = int(input(f"Введите x{i}: "))
    s = s + x
if s % b == 0:
    print("Да, сумма кратна b")
else:
    print("Нет, сумма не кратна b")
