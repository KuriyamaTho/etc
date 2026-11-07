by = int(input("Введите год рождения: "))
bm = int(input("Введите номер месяца рождения: "))
cy = int(input("Введите текущий год: "))
cm = int(input("Введите номер текущего месяца: "))
age = cy - by
if cm < bm:
    age = age - 1
print("Возраст (число полных лет):", age)
