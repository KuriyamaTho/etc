count1 = 0
time1 = 0
count2 = 0
time2 = 0
for i in range(1, 25):
    team = int(input(f"Удаление {i}, номер команды (1 или 2): "))
    minutes = int(input(f"Удаление {i}, продолжительность (2, 5 или 10 мин): "))
    if team == 1:
        count1 = count1 + 1
        time1 = time1 + minutes
    else:
        count2 = count2 + 1
        time2 = time2 + minutes
print("Команда 1: удалений", count1, ", общее время", time1, "мин")
print("Команда 2: удалений", count2, ", общее время", time2, "мин")
