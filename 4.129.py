by = int(input("Введите год рождения: "))
bm = int(input("Введите номер месяца рождения: "))
bd = int(input("Введите день рождения: "))
cy = int(input("Введите текущий год: "))
cm = int(input("Введите номер текущего месяца: "))
cd = int(input("Введите текущий день: "))
age = cy - by
if cm < bm or (cm == bm and cd < bd):
    age = age - 1
print("Возраст (число полных лет):", age)
