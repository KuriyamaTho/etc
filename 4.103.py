a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# а)
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print("а) Максимальное значение:", mx)

# б)
mn = a
if b < mn:
    mn = b
if c < mn:
    mn = c
print("б) Минимальное значение:", mn)
