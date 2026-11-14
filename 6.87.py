score1 = 0
score2 = 0
points = int(input("Введите количество очков (1, 2 или 3), 0 - конец игры: "))
while points != 0:
    team = int(input("Введите номер команды (1 или 2): "))
    if team == 1:
        score1 = score1 + points
    else:
        score2 = score2 + points
    print("Счет:", score1, ":", score2)
    points = int(input("Введите количество очков (1, 2 или 3), 0 - конец игры: "))
print("Игра окончена. Итоговый счет:", score1, ":", score2)
if score1 > score2:
    print("Победила команда 1")
elif score2 > score1:
    print("Победила команда 2")
else:
    print("Ничья")
