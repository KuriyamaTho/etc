m = int(input("Введите номер масти (1-4): "))
k = int(input("Введите номер достоинства карты (6-14): "))
match k:
    case 6:
        rank = "Шестерка"
    case 7:
        rank = "Семерка"
    case 8:
        rank = "Восьмерка"
    case 9:
        rank = "Девятка"
    case 10:
        rank = "Десятка"
    case 11:
        rank = "Валет"
    case 12:
        rank = "Дама"
    case 13:
        rank = "Король"
    case 14:
        rank = "Туз"
    case _:
        rank = "?"
match m:
    case 1:
        suit = "пик"
    case 2:
        suit = "треф"
    case 3:
        suit = "бубен"
    case 4:
        suit = "червей"
    case _:
        suit = "?"
print(rank, suit)
