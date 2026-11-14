found = False
i = 0
while i < 28 and not found:
    mark = int(input(f"Введите оценку ученика {i + 1}: "))
    i = i + 1
    found = mark == 2
if found:
    print("Да, среди оценок есть двойки")
else:
    print("Нет, двоек среди оценок нет")
