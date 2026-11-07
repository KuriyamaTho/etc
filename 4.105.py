n = int(input("Введите порядковый номер месяца (1-12): "))
match n:
    case 1:
        print("январь")
    case 2:
        print("февраль")
    case 3:
        print("март")
    case 4:
        print("апрель")
    case 5:
        print("май")
    case 6:
        print("июнь")
    case 7:
        print("июль")
    case 8:
        print("август")
    case 9:
        print("сентябрь")
    case 10:
        print("октябрь")
    case 11:
        print("ноябрь")
    case 12:
        print("декабрь")
    case _:
        print("Неверный номер месяца")
