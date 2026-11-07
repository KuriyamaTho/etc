for student in range(1, 3):
    s = 0
    for subject in range(1, 5):
        b = int(input(f"Ученик {student}, оценка по предмету {subject}: "))
        s = s + b
    print("Сумма оценок ученика", student, "=", s)
