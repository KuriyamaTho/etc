n = int(input("Введите натуральное число n: "))
x = int(input("Введите x1: "))
mx = x
mn = x
pos_mx = 1
pos_mn = 1
for i in range(2, n + 1):
    x = int(input(f"Введите x{i}: "))
    if x > mx:
        mx = x
        pos_mx = i
    if x < mn:
        mn = x
        pos_mn = i
if pos_mx < pos_mn:
    print("Раньше встретится максимальное число")
elif pos_mn < pos_mx:
    print("Раньше встретится минимальное число")
else:
    print("Максимальное и минимальное числа совпадают")
