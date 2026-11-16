print("1) Ввод и вывод по строкам")
for student in range(1, 19):
    for subject in range(1, 4):
        mark = int(input(f"Ученик {student}, предмет {subject}: "))
        print(f"Ученик {student}, предмет {subject}: {mark}")

print("2) Ввод и вывод по столбцам")
for subject in range(1, 4):
    for student in range(1, 19):
        mark = int(input(f"Предмет {subject}, ученик {student}: "))
        print(f"Предмет {subject}, ученик {student}: {mark}")
