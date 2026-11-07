a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
mx = a
mn = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if b < mn:
    mn = b
if c < mn:
    mn = c
print("Максимальное значение:", mx)
print("Минимальное значение:", mn)
