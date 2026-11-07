a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = int(input("Введите e: "))
f = int(input("Введите f: "))

if (((a == e) or (b == f)) and ((a != e) or (b != f))) and not (((c == e) or (d == f)) and ((c != e) or (d != f))):
    print("а) ладья и ладья: Да")
else:
    print("а) ладья и ладья: Нет")

if (((a == e) or (b == f)) and ((a != e) or (b != f))) and not ((((c == e) or (d == f)) or (abs(c - e) == abs(d - f))) and ((c != e) or (d != f))):
    print("б) ладья и ферзь: Да")
else:
    print("б) ладья и ферзь: Нет")

if (((a == e) or (b == f)) and ((a != e) or (b != f))) and not (((abs(c - e) == 1) and (abs(d - f) == 2)) or ((abs(c - e) == 2) and (abs(d - f) == 1))):
    print("в) ладья и конь: Да")
else:
    print("в) ладья и конь: Нет")

if (((a == e) or (b == f)) and ((a != e) or (b != f))) and not ((abs(c - e) == abs(d - f)) and (c != e)):
    print("г) ладья и слон: Да")
else:
    print("г) ладья и слон: Нет")

if ((((a == e) or (b == f)) or (abs(a - e) == abs(b - f))) and ((a != e) or (b != f))) and not ((((c == e) or (d == f)) or (abs(c - e) == abs(d - f))) and ((c != e) or (d != f))):
    print("д) ферзь и ферзь: Да")
else:
    print("д) ферзь и ферзь: Нет")

if ((((a == e) or (b == f)) or (abs(a - e) == abs(b - f))) and ((a != e) or (b != f))) and not (((c == e) or (d == f)) and ((c != e) or (d != f))):
    print("е) ферзь и ладья: Да")
else:
    print("е) ферзь и ладья: Нет")

if ((((a == e) or (b == f)) or (abs(a - e) == abs(b - f))) and ((a != e) or (b != f))) and not (((abs(c - e) == 1) and (abs(d - f) == 2)) or ((abs(c - e) == 2) and (abs(d - f) == 1))):
    print("ж) ферзь и конь: Да")
else:
    print("ж) ферзь и конь: Нет")

if ((((a == e) or (b == f)) or (abs(a - e) == abs(b - f))) and ((a != e) or (b != f))) and not ((abs(c - e) == abs(d - f)) and (c != e)):
    print("з) ферзь и слон: Да")
else:
    print("з) ферзь и слон: Нет")

if (((abs(a - e) == 1) and (abs(b - f) == 2)) or ((abs(a - e) == 2) and (abs(b - f) == 1))) and not (((abs(c - e) == 1) and (abs(d - f) == 2)) or ((abs(c - e) == 2) and (abs(d - f) == 1))):
    print("и) конь и конь: Да")
else:
    print("и) конь и конь: Нет")

if (((abs(a - e) == 1) and (abs(b - f) == 2)) or ((abs(a - e) == 2) and (abs(b - f) == 1))) and not (((c == e) or (d == f)) and ((c != e) or (d != f))):
    print("к) конь и ладья: Да")
else:
    print("к) конь и ладья: Нет")

if (((abs(a - e) == 1) and (abs(b - f) == 2)) or ((abs(a - e) == 2) and (abs(b - f) == 1))) and not ((((c == e) or (d == f)) or (abs(c - e) == abs(d - f))) and ((c != e) or (d != f))):
    print("л) конь и ферзь: Да")
else:
    print("л) конь и ферзь: Нет")

if (((abs(a - e) == 1) and (abs(b - f) == 2)) or ((abs(a - e) == 2) and (abs(b - f) == 1))) and not ((abs(c - e) == abs(d - f)) and (c != e)):
    print("м) конь и слон: Да")
else:
    print("м) конь и слон: Нет")

if ((abs(a - e) == abs(b - f)) and (a != e)) and not ((abs(c - e) == abs(d - f)) and (c != e)):
    print("н) слон и слон: Да")
else:
    print("н) слон и слон: Нет")

if ((abs(a - e) == abs(b - f)) and (a != e)) and not ((((c == e) or (d == f)) or (abs(c - e) == abs(d - f))) and ((c != e) or (d != f))):
    print("о) слон и ферзь: Да")
else:
    print("о) слон и ферзь: Нет")

if ((abs(a - e) == abs(b - f)) and (a != e)) and not (((abs(c - e) == 1) and (abs(d - f) == 2)) or ((abs(c - e) == 2) and (abs(d - f) == 1))):
    print("п) слон и конь: Да")
else:
    print("п) слон и конь: Нет")

if ((abs(a - e) == abs(b - f)) and (a != e)) and not (((c == e) or (d == f)) and ((c != e) or (d != f))):
    print("р) слон и ладья: Да")
else:
    print("р) слон и ладья: Нет")

if ((abs(a - e) <= 1) and (abs(b - f) <= 1) and ((a != e) or (b != f))) and not ((abs(c - e) == abs(d - f)) and (c != e)):
    print("с) король и слон: Да")
else:
    print("с) король и слон: Нет")

if ((abs(a - e) <= 1) and (abs(b - f) <= 1) and ((a != e) or (b != f))) and not ((((c == e) or (d == f)) or (abs(c - e) == abs(d - f))) and ((c != e) or (d != f))):
    print("т) король и ферзь: Да")
else:
    print("т) король и ферзь: Нет")

if ((abs(a - e) <= 1) and (abs(b - f) <= 1) and ((a != e) or (b != f))) and not (((abs(c - e) == 1) and (abs(d - f) == 2)) or ((abs(c - e) == 2) and (abs(d - f) == 1))):
    print("у) король и конь: Да")
else:
    print("у) король и конь: Нет")

if ((abs(a - e) <= 1) and (abs(b - f) <= 1) and ((a != e) or (b != f))) and not (((c == e) or (d == f)) and ((c != e) or (d != f))):
    print("ф) король и ладья: Да")
else:
    print("ф) король и ладья: Нет")
