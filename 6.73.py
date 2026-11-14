first = int(input("Введите a1: "))
i = 1
same = True
while i < 15 and same:
    x = int(input(f"Введите a{i + 1}: "))
    i = i + 1
    same = x == first
if same:
    print("Да, все элементы равны между собой")
else:
    print("Нет, не все элементы равны между собой")
