s = 0
for i in range(1, 16):
    c = float(input(f"Введите c{i}: "))
    if i % 2 == 1:
        s = s - c
print("Сумма -c1 - c3 - c5 - ... =", s)
