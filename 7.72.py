u = float(input("Введите напряжение на сопротивлении 1, В: "))
r = float(input("Введите сопротивление 1, Ом: "))
best = u / r
pos = 1
for i in range(2, 21):
    u = float(input(f"Введите напряжение на сопротивлении {i}, В: "))
    r = float(input(f"Введите сопротивление {i}, Ом: "))
    if u / r < best:
        best = u / r
        pos = i
print("Минимальный ток проходит по сопротивлению номер:", pos)
