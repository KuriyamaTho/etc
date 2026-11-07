n = int(input("Введите номер года n (n >= 1984): "))
animal = (n - 1984) % 12
color = (n - 1984) % 10 // 2
match animal:
    case 0:
        name = "Крыса"
    case 1:
        name = "Корова"
    case 2:
        name = "Тигр"
    case 3:
        name = "Заяц"
    case 4:
        name = "Дракон"
    case 5:
        name = "Змея"
    case 6:
        name = "Лошадь"
    case 7:
        name = "Овца"
    case 8:
        name = "Обезьяна"
    case 9:
        name = "Петух"
    case 10:
        name = "Собака"
    case _:
        name = "Свинья"
match color:
    case 0:
        col = "Зеленый"
    case 1:
        col = "Красный"
    case 2:
        col = "Желтый"
    case 3:
        col = "Белый"
    case _:
        col = "Черный"
print("а)", name + ", " + col)

n = int(input("Введите номер года n (любое натуральное число): "))
animal = (n - 1984) % 12
color = (n - 1984) % 10 // 2
match animal:
    case 0:
        name = "Крыса"
    case 1:
        name = "Корова"
    case 2:
        name = "Тигр"
    case 3:
        name = "Заяц"
    case 4:
        name = "Дракон"
    case 5:
        name = "Змея"
    case 6:
        name = "Лошадь"
    case 7:
        name = "Овца"
    case 8:
        name = "Обезьяна"
    case 9:
        name = "Петух"
    case 10:
        name = "Собака"
    case _:
        name = "Свинья"
match color:
    case 0:
        col = "Зеленый"
    case 1:
        col = "Красный"
    case 2:
        col = "Желтый"
    case 3:
        col = "Белый"
    case _:
        col = "Черный"
print("б)", name + ", " + col)
