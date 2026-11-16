n = int(input("Введите количество этапов: "))
t = float(input("Введите время на этапе 1, мин: "))
best = t
worst = t
pos_best = 1
pos_worst = 1
for i in range(2, n + 1):
    t = float(input(f"Введите время на этапе {i}, мин: "))
    if t < best:
        best = t
        pos_best = i
    if t > worst:
        worst = t
        pos_worst = i
if pos_best < pos_worst:
    print("Да, этап, который он выиграл, был раньше этапа, на котором он занял последнее место")
else:
    print("Нет, этап, который он выиграл, был позже этапа, на котором он занял последнее место")
