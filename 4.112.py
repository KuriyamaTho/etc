n = int(input("Введите количество прошедших месяцев n: "))
m = n % 12
match m:
    case 0:
        print("январь")
    case 1:
        print("февраль")
    case 2:
        print("март")
    case 3:
        print("апрель")
    case 4:
        print("май")
    case 5:
        print("июнь")
    case 6:
        print("июль")
    case 7:
        print("август")
    case 8:
        print("сентябрь")
    case 9:
        print("октябрь")
    case 10:
        print("ноябрь")
    case 11:
        print("декабрь")
