m = int(input("Введите натуральное число m: "))
n = int(input("Введите n: "))
s = 0
for i in range(1, m + 1):
    x = int(input(f"Введите x{i}: "))
    if x % n == 0:
        s = s + x
print("Сумма чисел, кратных n:", s)
