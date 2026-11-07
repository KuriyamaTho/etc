k = int(input("Введите номер карты (6-14): "))
match k:
    case 6:
        print("шестерка")
    case 7:
        print("семерка")
    case 8:
        print("восьмерка")
    case 9:
        print("девятка")
    case 10:
        print("десятка")
    case 11:
        print("валет")
    case 12:
        print("дама")
    case 13:
        print("король")
    case 14:
        print("туз")
    case _:
        print("Неверный номер карты")
