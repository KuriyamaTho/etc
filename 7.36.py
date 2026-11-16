n = int(input("Введите натуральное число n: "))
k = 0
x1 = float(input("Введите x1: "))
x2 = float(input("Введите x2: "))
for i in range(3, n + 1):
    x3 = float(input(f"Введите x{i}: "))
    if x2 > x1 and x2 > x3:
        k = k + 1
    x1 = x2
    x2 = x3
print("Количество чисел, больших своих соседей:", k)
