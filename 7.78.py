n = int(input("Введите натуральное число n: "))
best = 0
cur = 0
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a % 2 == 0:
        cur = cur + 1
        if cur > best:
            best = cur
    else:
        cur = 0
print("Наибольшая длина отрезка из четных чисел:", best)
