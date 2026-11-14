m = float(input("Введите число m: "))
g = float(input("Введите первый член прогрессии g: "))
z = float(input("Введите знаменатель прогрессии z: "))
if m == g:
    member = True
elif g == 0:
    member = False
elif z == 0:
    member = m == 0
elif m == 0:
    member = False
elif abs(z) == 1:
    member = z == -1 and m == -g
else:
    t = g
    if abs(z) > 1:
        while abs(t) < abs(m) - 1e-12:
            t = t * z
    else:
        while abs(t) > abs(m) + 1e-12:
            t = t * z
    member = abs(t - m) < 1e-9 * max(1, abs(m))
if member:
    print("Да, число является членом геометрической прогрессии")
else:
    print("Нет, число не является членом геометрической прогрессии")
