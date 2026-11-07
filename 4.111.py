k = int(input("Введите номер дня года k (1 <= k <= 365): "))

# а)
n = (k - 1) % 7
print("а) k-й день года:")
match n:
    case 0:
        print("понедельник")
    case 1:
        print("вторник")
    case 2:
        print("среда")
    case 3:
        print("четверг")
    case 4:
        print("пятница")
    case 5:
        print("суббота")
    case 6:
        print("воскресенье")

# б)
d = int(input("б) Введите номер дня недели d, на который приходится 1 января (1-7): "))
n = (k - 1 + d - 1) % 7
print("б) k-й день года:")
match n:
    case 0:
        print("понедельник")
    case 1:
        print("вторник")
    case 2:
        print("среда")
    case 3:
        print("четверг")
    case 4:
        print("пятница")
    case 5:
        print("суббота")
    case 6:
        print("воскресенье")
