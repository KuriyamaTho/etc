n = int(input("Введите количество квартир: "))
mx = -1
pos = 0
for i in range(1, n + 1):
    k = int(input(f"Введите число жильцов квартиры {i}: "))
    if k >= mx:
        mx = k
        pos = i
print("Больше всего жильцов в квартире:", pos)
