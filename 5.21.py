price = float(input("Введите стоимость 1 кг сыра: "))
for g in range(50, 1001, 50):
    print(g, "г -", f"{price * g / 1000:.2f}")
