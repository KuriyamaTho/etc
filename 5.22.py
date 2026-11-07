price = float(input("Введите стоимость 1 кг конфет: "))
for g in range(100, 2001, 100):
    print(g, "г -", f"{price * g / 1000:.2f}")
