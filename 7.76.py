n = int(input("Введите количество дней в месяце: "))
t = float(input("Введите температуру за 1 число: "))
mn = t
count = 1
for i in range(2, n + 1):
    t = float(input(f"Введите температуру за {i} число: "))
    if t < mn:
        mn = t
        count = 1
    elif t == mn:
        count = count + 1
print("Дней с самой низкой температурой было:", count)
