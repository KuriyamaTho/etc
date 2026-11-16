i = 0
no_three = True
while i < 12 and no_three:
    m = int(input(f"Введите оценку по предмету {i + 1}: "))
    i = i + 1
    no_three = m != 3
if no_three:
    print("Да, среди оценок нет троек")
else:
    print("Нет, среди оценок есть тройки")
