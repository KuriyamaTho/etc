wins = 0
draws = 0
losses = 0
big = 0
points = 0
for i in range(1, 21):
    a = int(input(f"Игра {i}, забито мячей: "))
    b = int(input(f"Игра {i}, пропущено мячей: "))
    if a > b:
        print("а) Игра", i, ": выигрыш")
        wins = wins + 1
        points = points + 3
    elif a == b:
        print("а) Игра", i, ": ничья")
        draws = draws + 1
        points = points + 1
    else:
        print("а) Игра", i, ": проигрыш")
        losses = losses + 1
    if a - b >= 3:
        big = big + 1
print("б) Количество выигрышей:", wins)
print("в) Количество выигрышей:", wins, ", количество проигрышей:", losses)
print("г) Выигрышей:", wins, ", ничьих:", draws, ", проигрышей:", losses)
print("д) Игр с разностью мячей, большей или равной трем:", big)
print("е) Общее число очков:", points)
