a1 = float(input("Введите размер чемодана a1, см: "))
a2 = float(input("Введите размер чемодана a2, см: "))
a3 = float(input("Введите размер чемодана a3, см: "))
b1 = float(input("Введите размер коробки b1, см: "))
b2 = float(input("Введите размер коробки b2, см: "))
b3 = float(input("Введите размер коробки b3, см: "))
suitcase = sorted([a1, a2, a3])
box = sorted([b1, b2, b3])
if box[0] <= suitcase[0] and box[1] <= suitcase[1] and box[2] <= suitcase[2]:
    print("Да, пассажир сможет сэкономить, поместив коробку в чемодан")
else:
    print("Нет, коробка не помещается в чемодан")
