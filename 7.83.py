n = int(input("Введите n (n >= 4): "))
inf = float("inf")
v1 = inf
v2 = inf
v3 = inf
v4 = inf
i1 = 0
i2 = 0
i3 = 0
i4 = 0
for i in range(1, n + 1):
    a = int(input(f"Введите результат спортсмена {i} (в сотых долях секунды): "))
    if a < v1:
        v4, i4 = v3, i3
        v3, i3 = v2, i2
        v2, i2 = v1, i1
        v1, i1 = a, i
    elif a < v2:
        v4, i4 = v3, i3
        v3, i3 = v2, i2
        v2, i2 = a, i
    elif a < v3:
        v4, i4 = v3, i3
        v3, i3 = a, i
    elif a < v4:
        v4, i4 = a, i
numbers = sorted([i1, i2, i3, i4])
print("Номера четырех лучших бегунов i, j, k, m:", numbers[0], numbers[1], numbers[2], numbers[3])
print("Сумма результатов:", v1 + v2 + v3 + v4)
