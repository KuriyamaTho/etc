n = int(input("Введите количество людей в группе: "))
h = float(input("Введите рост человека 1: "))
mx = h
mn = h
for i in range(2, n + 1):
    h = float(input(f"Введите рост человека {i}: "))
    if h > mx:
        mx = h
    if h < mn:
        mn = h
print("Рост самого высокого превышает рост самого низкого на:", mx - mn)
