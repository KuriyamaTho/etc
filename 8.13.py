fives = 0
t1 = 0
t2 = 0
t3 = 0
for student in range(1, 19):
    threes = 0
    for subject in range(1, 4):
        m = int(input(f"Ученик {student}, оценка по предмету {subject}: "))
        if m == 5:
            fives = fives + 1
        if m == 3:
            threes = threes + 1
        if m == 2:
            if subject == 1:
                t1 = t1 + 1
            elif subject == 2:
                t2 = t2 + 1
            else:
                t3 = t3 + 1
    print("б) Количество троек у ученика", student, ":", threes)
print("а) Общее количество пятерок в таблице:", fives)
print("в) Количество двоек по предмету 1:", t1)
print("в) Количество двоек по предмету 2:", t2)
print("в) Количество двоек по предмету 3:", t3)
