for cls in range(1, 3):
    s = 0
    for i in range(1, 21):
        age = float(input(f"Класс {cls}, возраст ученика {i}: "))
        s = s + age
    print("Средний возраст учеников класса", cls, "=", s / 20)
