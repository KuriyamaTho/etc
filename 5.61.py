n = int(input("Введите численность каждого класса: "))
for cls in range(1, 3):
    s = 0
    for i in range(1, n + 1):
        h = float(input(f"Класс {cls}, рост ученика {i}: "))
        s = s + h
    print("Средний рост учеников класса", cls, "=", s / n)
