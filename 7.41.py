n = int(input("Введите количество учеников в классе: "))
k5 = 0
k4 = 0
k3 = 0
k2 = 0
for i in range(1, n + 1):
    m = int(input(f"Введите оценку ученика {i}: "))
    if m == 5:
        k5 = k5 + 1
    elif m == 4:
        k4 = k4 + 1
    elif m == 3:
        k3 = k3 + 1
    elif m == 2:
        k2 = k2 + 1
print("Пятерок:", k5)
print("Четверок:", k4)
print("Троек:", k3)
print("Двоек:", k2)
