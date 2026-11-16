n = int(input("Введите натуральное число n: "))
x = float(input("Введите x1: "))
mx = x
mn = x
for i in range(2, n + 1):
    x = float(input(f"Введите x{i}: "))
    if x > mx:
        mx = x
    if x < mn:
        mn = x
print("а) Максимальное число:", mx)
print("б) Минимальное число:", mn)
print("в) Максимальное число:", mx, ", минимальное число:", mn)
