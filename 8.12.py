p1 = 0
p2 = 0
p3 = 0
for athlete in range(1, 16):
    s = 0
    for program in range(1, 4):
        b = float(input(f"Спортсмен {athlete}, баллы за программу {program}: "))
        s = s + b
        if program == 1:
            p1 = p1 + b
        elif program == 2:
            p2 = p2 + b
        else:
            p3 = p3 + b
    print("а) Среднее количество баллов спортсмена", athlete, ":", s / 3)
print("б) Среднее количество баллов по обязательной программе:", p1 / 15)
print("б) Среднее количество баллов по короткой программе:", p2 / 15)
print("б) Среднее количество баллов по произвольной программе:", p3 / 15)
