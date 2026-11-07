a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
mn = a
if b < mn:
    mn = b
if c < mn:
    mn = c
print("Сумма двух наибольших чисел:", a + b + c - mn)
