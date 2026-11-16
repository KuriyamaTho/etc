a = int(input("Введите a: "))
b = int(input("Введите b: "))
best = -1
best_n = 0
for n in range(a, b + 1):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s = s + d
    if s > best:
        best = s
        best_n = n
print("Число с максимальной суммой делителей:", best_n)
print("Сумма делителей:", best)
