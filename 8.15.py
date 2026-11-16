mx = 0
best = 0
for athlete in range(1, 9):
    s = 0
    for sport in range(1, 6):
        b = int(input(f"Спортсмен {athlete}, баллы по виду спорта {sport}: "))
        s = s + b
        if b > mx:
            mx = b
    if s > best:
        best = s
print("а) Максимальная оценка в таблице:", mx)
print("б) Баллов набрал победитель соревнований:", best)
