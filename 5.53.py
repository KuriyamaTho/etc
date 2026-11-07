s = 0
for i in range(1, 11):
    b = int(input(f"Введите оценку по предмету {i}: "))
    s = s + b
print("Средняя оценка =", s / 10)
