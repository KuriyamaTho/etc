for athlete in range(1, 3):
    s = 0
    for sport in range(1, 6):
        b = float(input(f"Спортсмен {athlete}, баллы в виде спорта {sport}: "))
        s = s + b
    print("Сумма баллов спортсмена", athlete, "=", s)
