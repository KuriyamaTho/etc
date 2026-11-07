a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))

if ((a == c) or (b == d)) and ((a != c) or (b != d)):
    print("а) Да")
else:
    print("а) Нет")

if (abs(a - c) == abs(b - d)) and (a != c):
    print("б) Да")
else:
    print("б) Нет")

if (abs(a - c) <= 1) and (abs(b - d) <= 1) and ((a != c) or (b != d)):
    print("в) Да")
else:
    print("в) Нет")

if (((a == c) or (b == d)) or (abs(a - c) == abs(b - d))) and ((a != c) or (b != d)):
    print("г) Да")
else:
    print("г) Нет")

if (c == a) and ((d == b + 1) or ((b == 2) and (d == 4))):
    print("д) при обычном ходе: Да")
else:
    print("д) при обычном ходе: Нет")
if (abs(c - a) == 1) and (d == b + 1):
    print("д) когда бьет: Да")
else:
    print("д) когда бьет: Нет")

if (c == a) and ((d == b - 1) or ((b == 7) and (d == 5))):
    print("е) при обычном ходе: Да")
else:
    print("е) при обычном ходе: Нет")
if (abs(c - a) == 1) and (d == b - 1):
    print("е) когда бьет: Да")
else:
    print("е) когда бьет: Нет")

if ((abs(a - c) == 1) and (abs(b - d) == 2)) or ((abs(a - c) == 2) and (abs(b - d) == 1)):
    print("ж) Да")
else:
    print("ж) Нет")
