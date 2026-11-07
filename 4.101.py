a1 = float(input("Первая тройка, число 1: "))
a2 = float(input("Первая тройка, число 2: "))
a3 = float(input("Первая тройка, число 3: "))
b1 = float(input("Вторая тройка, число 1: "))
b2 = float(input("Вторая тройка, число 2: "))
b3 = float(input("Вторая тройка, число 3: "))

mx = a1
mn = a1
if a2 > mx:
    mx = a2
if a3 > mx:
    mx = a3
if a2 < mn:
    mn = a2
if a3 < mn:
    mn = a3
mid1 = a1 + a2 + a3 - mx - mn

mx = b1
mn = b1
if b2 > mx:
    mx = b2
if b3 > mx:
    mx = b3
if b2 < mn:
    mn = b2
if b3 < mn:
    mn = b3
mid2 = b1 + b2 + b3 - mx - mn

print("Среднее арифметическое средних чисел:", (mid1 + mid2) / 2)
