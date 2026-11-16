n = int(input("Введите количество людей в группе: "))
before = 0
after = 0
for i in range(1, n + 1):
    y = int(input(f"Введите год рождения человека {i}: "))
    if y < 1985:
        before = before + 1
    if y > 1990:
        after = after + 1
print("Родились до 1985 года:", before)
print("Родились после 1990 года:", after)
