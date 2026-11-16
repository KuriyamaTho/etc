n = int(input("Введите количество учеников в классе: "))
fives = 0
twos = 0
for i in range(1, n + 1):
    m = int(input(f"Введите оценку ученика {i}: "))
    if m == 5:
        fives = fives + 1
    if m == 2:
        twos = twos + 1
print("Количество пятерок:", fives)
print("Количество двоек:", twos)
