m = int(input("Введите номер масти (1-4): "))
match m:
    case 1:
        print("пики")
    case 2:
        print("трефы")
    case 3:
        print("бубны")
    case 4:
        print("червы")
    case _:
        print("Неверный номер масти")
