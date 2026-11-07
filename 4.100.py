a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if mx == a:
    p = b * c
elif mx == b:
    p = a * c
else:
    p = a * b
print("Произведение двух наименьших чисел:", p)
