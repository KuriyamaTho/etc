n = int(input("Введите натуральное число (не менее двух цифр): "))
mx1 = -1
mx2 = -1
mn1 = 10
mn2 = 10
while n > 0:
    d = n % 10
    if d > mx1:
        mx2 = mx1
        mx1 = d
    elif d > mx2:
        mx2 = d
    if d < mn1:
        mn2 = mn1
        mn1 = d
    elif d < mn2:
        mn2 = d
    n = n // 10
print("а) Две максимальные цифры:", mx1, mx2)
print("б) Две минимальные цифры:", mn1, mn2)
