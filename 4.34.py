a = int(input("Введите a: "))
b = int(input("Введите b: "))
if b % a == 0:
    print("Да, a является делителем b")
else:
    print("Нет, a не является делителем b")
if a % b == 0:
    print("Да, b является делителем a")
else:
    print("Нет, b не является делителем a")
