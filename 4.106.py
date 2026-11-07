n = int(input("Введите порядковый номер месяца (1-12): "))
match n:
    case 12 | 1 | 2:
        print("зима")
    case 3 | 4 | 5:
        print("весна")
    case 6 | 7 | 8:
        print("лето")
    case 9 | 10 | 11:
        print("осень")
    case _:
        print("Неверный номер месяца")
