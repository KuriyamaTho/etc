n = int(input("Введите номер дня недели (1-7): "))
match n:
    case 1:
        print("понедельник")
    case 2:
        print("вторник")
    case 3:
        print("среда")
    case 4:
        print("четверг")
    case 5:
        print("пятница")
    case 6:
        print("суббота")
    case 7:
        print("воскресенье")
    case _:
        print("Неверный номер дня недели")
