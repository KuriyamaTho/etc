best_group = 0
best_avg = -1
for group in range(1, 4):
    s = 0
    for student in range(1, 21):
        for exam in range(1, 4):
            m = int(input(f"Группа {group}, студент {student}, экзамен {exam}: "))
            s = s + m
    avg = s / 60
    print("Средний балл группы", group, ":", avg)
    if avg > best_avg:
        best_avg = avg
        best_group = group
print("Лучшая по среднему баллу группа:", best_group)
