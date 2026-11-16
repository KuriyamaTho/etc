n = int(input("Введите количество проведенных игр: "))
wins = 0
losses = 0
draws = 0
for i in range(1, n + 1):
    p = int(input(f"Введите число очков за игру {i} (0, 1 или 3): "))
    if p == 3:
        wins = wins + 1
    elif p == 1:
        draws = draws + 1
    else:
        losses = losses + 1
print("Выигрышей:", wins)
print("Проигрышей:", losses)
print("Ничьих:", draws)
