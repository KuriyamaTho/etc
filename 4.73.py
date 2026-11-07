a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвертое число: "))

# а)
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if d > mx:
    mx = d
print("а) Наибольшее число:", mx)

# б)
mn = a
if b < mn:
    mn = b
if c < mn:
    mn = c
if d < mn:
    mn = d
print("б) Наименьшее число:", mn)
