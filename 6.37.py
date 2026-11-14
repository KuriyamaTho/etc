count1 = 0
time1 = 0
count2 = 0
time2 = 0
team = int(input("Введите номер команды (1 или 2), 0 - конец игры: "))
while team != 0:
    minutes = int(input("Введите штрафное время (2, 5 или 10 мин): "))
    if team == 1:
        count1 = count1 + 1
        time1 = time1 + minutes
    else:
        count2 = count2 + 1
        time2 = time2 + minutes
    team = int(input("Введите номер команды (1 или 2), 0 - конец игры: "))
print("Команда 1: удалений", count1, ", штрафное время", time1, "мин")
print("Команда 2: удалений", count2, ", штрафное время", time2, "мин")
