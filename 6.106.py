a = int(input("Введите a: "))
b = int(input("Введите b (a > b): "))
q = 0
r = a
while r >= b:
    r = r - b
    q = q + 1
print("а) Результат целочисленного деления:", q)
print("б) Остаток от деления:", r)
