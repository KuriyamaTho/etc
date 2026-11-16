s = float(input("Введите длину участка автомобиля 1, км: "))
t = float(input("Введите время автомобиля 1, ч: "))
best = s / t
pos = 1
for i in range(2, 26):
    s = float(input(f"Введите длину участка автомобиля {i}, км: "))
    t = float(input(f"Введите время автомобиля {i}, ч: "))
    if s / t > best:
        best = s / t
        pos = i
print("Максимальная средняя скорость у автомобиля номер:", pos)
