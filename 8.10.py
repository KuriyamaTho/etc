print("1) Ввод по столбцам")
for sport in range(1, 6):
    for athlete in range(1, 9):
        points = int(input(f"Вид спорта {sport}, спортсмен {athlete}: "))
        print(f"Вид спорта {sport}, спортсмен {athlete}: {points}")

print("2) Ввод по строкам")
for athlete in range(1, 9):
    for sport in range(1, 6):
        points = int(input(f"Спортсмен {athlete}, вид спорта {sport}: "))
        print(f"Спортсмен {athlete}, вид спорта {sport}: {points}")
