pos = 0
prev = float(input("Введите a1: "))
i = 1
while i < 15 and pos == 0:
    x = float(input(f"Введите a{i + 1}: "))
    i = i + 1
    if x <= prev:
        pos = i
    prev = x
if pos == 0:
    print("Да, последовательность упорядочена по возрастанию")
else:
    print("Нет, первое число, нарушающее упорядоченность, имеет номер", pos)
