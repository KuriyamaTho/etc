n = int(input("Введите количество учащихся в каждом классе: "))
for cls in range(1, 3):
    s = 0
    for i in range(1, n + 1):
        b = int(input(f"Класс {cls}, оценка ученика {i}: "))
        s = s + b
    print("Средняя оценка в классе", cls, "=", s / n)
