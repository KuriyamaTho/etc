no_twos = 0
ok1 = True
ok2 = True
ok3 = True
t1 = 0
t2 = 0
t3 = 0
for student in range(1, 16):
    has_two = False
    for subject in range(1, 4):
        m = int(input(f"Студент {student}, оценка по предмету {subject}: "))
        if m == 2:
            has_two = True
        if m < 4:
            if subject == 1:
                ok1 = False
            elif subject == 2:
                ok2 = False
            else:
                ok3 = False
        if m == 2:
            if subject == 1:
                t1 = t1 + 1
            elif subject == 2:
                t2 = t2 + 1
            else:
                t3 = t3 + 1
    if not has_two:
        no_twos = no_twos + 1
k = 0
if ok1:
    k = k + 1
if ok2:
    k = k + 1
if ok3:
    k = k + 1
print("а) Количество студентов, сдавших сессию без двоек:", no_twos)
print("б) Количество предметов, по которым были только оценки 5 и 4:", k)
print("в) Количество двоек по предмету 1:", t1)
print("в) Количество двоек по предмету 2:", t2)
print("в) Количество двоек по предмету 3:", t3)
