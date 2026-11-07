s = 0
for i in range(1, 21):
    b = int(input(f"Введите оценку ученика {i}: "))
    s = s + b
print("Средняя оценка =", s / 20)
