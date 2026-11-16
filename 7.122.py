n = int(input("Введите количество людей в списке: "))
age = int(input("Введите возраст человека 1: "))
oldest = age
youngest = age
pos_old = 1
pos_young = 1
for i in range(2, n + 1):
    age = int(input(f"Введите возраст человека {i}: "))
    if age > oldest:
        oldest = age
        pos_old = i
    if age < youngest:
        youngest = age
        pos_young = i
if pos_old < pos_young:
    print("Раньше в списке указан самый старший человек")
elif pos_young < pos_old:
    print("Раньше в списке указан самый молодой человек")
else:
    print("Самый старший и самый молодой человек совпадают")
